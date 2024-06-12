from fastapi import FastAPI, APIRouter, Form

#from .views import user_router, assets_router
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import List

from .schemas import (
   UserCreateInput, StandardOutput, 
   ErrorOutput, UserFavoriteAdd, UserListOutput
   )
from .services import UserService, FavoriteService


app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello world!'

STATIC_PATH = Path(__file__).resolve().parent / "static"
TEMPLATE_PATH = Path(__file__).resolve().parent / "templates"

#user_router = APIRouter(prefix='/user')
#assets_router = APIRouter(prefix='/assets')

static = StaticFiles(directory=STATIC_PATH)
templates = Jinja2Templates(directory=TEMPLATE_PATH)

app.mount("/static", static, name="static")
#app.include_router(prefix='/first',router=router)
#app.include_router(user_router)
#app.include_router(assets_router)

# USERS
@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/home", response_class=HTMLResponse, include_in_schema=False)
async def render_home(request: Request):
   return templates.TemplateResponse(request=request, name="index.html")

@app.get("/create", response_class=HTMLResponse, include_in_schema=False)
async def render_home(request: Request):
   return templates.TemplateResponse(request=request, name="cadastro.html")

@app.get("/ativos", response_class=HTMLResponse, include_in_schema=False)
async def render_home(request: Request):
   return templates.TemplateResponse(request=request, name="ativos.html")

@app.post('/create', description='Adds a new user to the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_create(name:str = Form(...)):
    try:
       user_item = UserCreateInput(name=name)
       await UserService.create_user(name=user_item.name)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@app.delete('/delete/{user_id}', description='deletes a user from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_delete(user_id):
    try:
       await UserService.delete_user(user_id)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))
    
@app.post('/favorite/add', description='Adds a favorite to the user', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAdd):
    try:
       await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@app.delete('/favorite/remove/{user_id}', description='deletes a favorite from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_remove(user_id:int, symbol: str):
    try:
       await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
       return StandardOutput(message='Ok')
    except Exception as e:
       raise HTTPException(400, detail=str(e))  
      
@app.get('/list', description='List Users from the database', response_model=List[UserListOutput], responses={400:{'model': ErrorOutput}})
async def user_list():
    try:
       return await UserService.list_user()
    except Exception as e:
       raise HTTPException(400, detail=str(e))    