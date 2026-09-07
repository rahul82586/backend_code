"""
Account REST API Router

Exposes client endpoints for querying real-time account snapshots and open positions.

Architectural Rule: Invokes CQRS Query Handlers, zero direct DB access.
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from api.auth.dependencies import get_current_user
from api.di_providers import get_account_info_query_handler, get_positions_query_handler
from api.schemas.account import AccountInfo, PositionResponse
from application.queries.get_account_info import GetAccountInfoQuery, GetAccountInfoQueryHandler
from application.queries.get_positions import GetPositionsQuery, GetPositionsQueryHandler
from core.domains.accounts.models import Account

router = APIRouter(prefix="/api/v1/account", tags=["Account"])


@router.get("/info", response_model=AccountInfo)
async def get_account_info(
    current_user: Account = Depends(get_current_user),
    handler: GetAccountInfoQueryHandler = Depends(get_account_info_query_handler)
):
    """Get current account metrics (balance, equity, margin usage, margin level)."""
    try:
        query = GetAccountInfoQuery(login_id=current_user.login_id)
        result = await handler.handle(query)
        return AccountInfo(**result)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/positions", response_model=List[PositionResponse])
async def get_open_positions(
    current_user: Account = Depends(get_current_user),
    handler: GetPositionsQueryHandler = Depends(get_positions_query_handler)
):
    """Get all active open positions for the authenticated user."""
    query = GetPositionsQuery(account_login=current_user.login_id)
    positions_list = await handler.handle(query)
    return [PositionResponse(**p) for p in positions_list]
