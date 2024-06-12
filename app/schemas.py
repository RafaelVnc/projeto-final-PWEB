from pydantic import BaseModel
from typing import List


class UserCreateInput(BaseModel):
    name: str


class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int
    #Casting database obj to json
    #class Config:
    #    orm_mode = True

class UserListDelete(BaseModel):
    id: int
    name: str

class UserListOutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]
    #Casting database obj to json
    #class Config:
    #    orm_mode = True