from domain.user.entities import User
from domain.user.user_repository import UserRepository
import bcrypt

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo: UserRepository = user_repo

    def hash_password(self, password: str) -> str:
        if not password or len(password) < 6:
            raise ValueError(f"Password must be at least 6 characters long, got: {repr(password)}")
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    async def create_user(self, username: str, email: str, password: str) -> User:
        hashed_password = self.hash_password(password)
        
        user = User(
            id=None,
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        await self.user_repo.save(user)
        return user

    async def list_users(self) -> list[User]:
        return await self.user_repo.list()
