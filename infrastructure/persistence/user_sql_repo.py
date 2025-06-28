from sqlalchemy import select
from infrastructure.pydantic_models.user_model import UserModel
from domain.user.entities import User
from domain.user.user_repository import UserRepository
from infrastructure.database.dependencies import get_session

class UserSQLRepository(UserRepository):
    async def save(self, user: User) -> None:
        async with get_session() as session:
            db_user = UserModel(
                username=user.username,
                email=user.email,
                hashed_password=user.hashed_password
            )
            session.add(db_user)
            await session.commit()
            await session.refresh(db_user)
            user.id = db_user.id

    async def list(self) -> list[User]:
        async with get_session() as session:
            result = await session.execute(select(UserModel))
            rows = result.scalars().all()
            return [
                User(
                    id=row.id,
                    username=row.username,
                    email=row.email,
                    hashed_password=row.hashed_password
                )
                for row in rows
            ]
