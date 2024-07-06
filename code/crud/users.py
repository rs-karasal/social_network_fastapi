from select import select
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User


async def get_all_users(
        session: AsyncSession
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()
