from typing import List
from fastapi import APIRouter, HTTPException

from .schemas import (
   UserCreateInput, StandardOutput, 
   ErrorOutput, UserFavoriteAdd, UserListOutput
   )
from .services import UserService, FavoriteService

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', description='Adds a new user to the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
       await UserService.create_user(name=user_input.name)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@user_router.delete('/delete/{user_id}', description='deletes a user from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_delete(user_id):
    try:
       await UserService.delete_user(user_id)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))
    
@user_router.post('/favorite/add', description='Adds a favorite to the user', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAdd):
    try:
       await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@user_router.delete('/favorite/remove/{user_id}', description='deletes a favorite from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_remove(user_id:int, symbol: str):
    try:
       await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))  
      
@user_router.get('/list', description='List Users from the database', response_model=List[UserListOutput], responses={400:{'model': ErrorOutput}})
async def user_list():
    try:
       return await UserService.list_user()
    except Exception as e:
       raise HTTPException(400, detail=str(e))    
