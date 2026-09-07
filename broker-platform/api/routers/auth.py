"""
Authentication REST API Router

Exposes client login endpoints for token issuance.
"""
from fastapi import APIRouter, Depends, HTTPException, status

from api.auth.jwt_handler import create_access_token
from api.di_providers import get_account_repo
from api.schemas.account import LoginRequest, TokenResponse
from core.ports.interfaces import IAccountRepository

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest,
    account_repo: IAccountRepository = Depends(get_account_repo)
):
    """Authenticate client login and issue JWT access token."""
    account = await account_repo.find_by_login(request.login_id)
    if not account or not getattr(account, "is_enabled", True):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials or account disabled"
        )

    access_token = create_access_token(data={"sub": account.login_id})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=86400
    )
