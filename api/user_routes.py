from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from use_cases.user_service import UserService
from infrastructure.persistence.user_sql_repo import UserSQLRepository

router = APIRouter()

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserReadDTO(BaseModel):
    id: str
    username: str
    email: str

def get_user_service() -> UserService:
    repo = UserSQLRepository()
    return UserService(repo)

@router.post("/users", response_model=UserReadDTO)
async def create_user(
    data: UserCreateDTO,
    service: UserService = Depends(get_user_service)
):
    user = await service.create_user(data.username, data.email, data.password)
    return UserReadDTO(
        id=str(user.id),
        username=user.username,
        email=user.email
    )

@router.get("/users", response_model=List[UserReadDTO])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    users = await service.list_users()
    return [
        UserReadDTO(
            id=str(u.id),
            username=u.username,
            email=u.email
        ) for u in users
    ]
