from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select
import asyncio

async def add_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            new_user = User(tg_id=tg_id)
            session.add(new_user)

            await session.flush()
            await session.commit()
