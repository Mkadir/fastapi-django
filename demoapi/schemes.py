from pydantic import BaseModel


class DemoUserBase(BaseModel):
    username: str
    age: int


class DemoUserDisplay(BaseModel):
    username: str
    age: int

    class Config:
        orm_mode = True
