from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

        extra_schema = {
            "id": 1,
            "name": "hoge",
        }


class UserCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

        extra_schema = {
            "id": 1,
            "name": "hoge",
        }


class UserCreateResponse(UserCreate):
    id: int
