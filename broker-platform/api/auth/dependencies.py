"""
Client Authentication Dependencies for FastAPI.

Injects current authenticated client user account into protected endpoints via OAuth2 Bearer token,
enforcing token revocation blacklist checks and rate limits.
"""
from typing import Optional
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

from api.auth.jwt_handler import verify_token
from api.di_providers import get_account_repo, get_token_blacklist, get_rate_limiter
from core.domains.accounts.models import Account
from core.ports.interfaces import IAccountRepository, ITokenBlacklist, IRateLimiter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    account_repo: IAccountRepository = Depends(get_account_repo),
    token_blacklist: Optional[ITokenBlacklist] = Depends(get_token_blacklist)
) -> Account:
    """FastAPI dependency resolving the authenticated client Account, with token revocation check."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if token_blacklist:
        if await token_blacklist.is_blacklisted(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been revoked",
                headers={"WWW-Authenticate": "Bearer"},
            )

    try:
        payload = verify_token(token)
        login_id: str = payload.get("sub")
    except Exception:
        raise credentials_exception

    account = await account_repo.find_by_login(login_id)
    if account is None:
        raise credentials_exception

    return account


async def require_rate_limit(
    request: Request,
    login_id: Optional[str] = None,
    rate_limiter: Optional[IRateLimiter] = Depends(get_rate_limiter)
) -> None:
    """
    FastAPI dependency enforcing dual sliding-window rate limiting on IP address and Login ID.
    Raises 429 Too Many Requests if rate limit is exceeded.
    """
    if not rate_limiter:
        return

    client_ip = request.client.host if request.client else "127.0.0.1"

    # Rate limit by IP (20 req / 60s)
    if not await rate_limiter.is_allowed(f"rate_limit:ip:{client_ip}", limit=20, window_seconds=60):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded for IP address"
        )

    # Rate limit by Login ID if provided (5 req / 60s)
    if login_id:
        if not await rate_limiter.is_allowed(f"rate_limit:login:{login_id}", limit=5, window_seconds=60):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded for login ID"
            )
