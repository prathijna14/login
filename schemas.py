from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    user_id: str
    name: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    name: str
    password: str
