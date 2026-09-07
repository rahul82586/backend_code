"""
Client Authentication Dependencies for FastAPI

Injects current authenticated client user account into protected endpoints via OAuth2 Bearer token.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from api.auth.jwt_handler import verify_token
from api.di_providers import get_account_repo
from core.domains.accounts.models import Account
from core.ports.interfaces import IAccountRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    account_repo: IAccountRepository = Depends(get_account_repo)
) -> Account:
    """FastAPI dependency resolving the authenticated client Account."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
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
