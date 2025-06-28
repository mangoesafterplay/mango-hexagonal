from abc import ABC, abstractmethod
from typing import List
from .entities import User

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def list(self) -> List[User]:
        pass
