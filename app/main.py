from fastapi import FastAPI, APIRouter, Form, HTTPException

#from .views import user_router, assets_router
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


from .schemas import (
   UserCreateInput, StandardOutput, 
   ErrorOutput, 
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

#HOME
@app.get("/home", response_class=HTMLResponse, include_in_schema=False)
async def render_home(request: Request):
   return templates.TemplateResponse(request=request, name="index.html")

#USERS
@app.get("/cadastro", response_class=HTMLResponse, include_in_schema=False)
async def render_create(request: Request):
   users = await UserService.list_user()
   return templates.TemplateResponse("cadastro.html", {"request": request, "users": users})

@app.get("/ativos", response_class=HTMLResponse, include_in_schema=False)
async def render_ativos(request: Request):
   users = await UserService.list_user()
   return templates.TemplateResponse("ativos.html", {"request": request, "users": users})

@app.get("/list", response_class=HTMLResponse, include_in_schema=False)
async def render_users(request: Request):
   users = await UserService.list_user()
   return templates.TemplateResponse("listagem.html", {"request": request, "users": users})

@app.post('/create', description='Adds a new user to the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_create(name:str = Form(...)):
    try:
       user_item = UserCreateInput(name=name)
       await UserService.create_user(name=user_item.name)
       return RedirectResponse(url='/cadastro', status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@app.delete('/delete', description='Deletes a user from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_delete(user_id: int = Form(...)):
    try:
       await UserService.delete_user(user_id)
       return RedirectResponse(url='/cadastro', status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))
    
@app.post('/favorite/add', description='Adds a favorite to the user', response_class=RedirectResponse, responses={400:{'model': ErrorOutput}})
async def user_favorite_add(user_id: int = Form(...), symbol: str = Form(...)):
    try:
       await FavoriteService.add_favorite(user_id=user_id, symbol=symbol)
       return RedirectResponse(url="/ativos", status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@app.delete('/favorite/remove/{user_id}', description='deletes a favorite from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_remove(user_id:int, symbol: str):
    try:
       await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
       return RedirectResponse(url="/ativos", status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))  
      
# @app.get('/list', description='List Users from the database', response_model=List[UserListOutput], responses={400:{'model': ErrorOutput}})
# async def user_list():
#     try:
#        return await UserService.list_user()
#     except Exception as e:
#        raise HTTPException(400, detail=str(e))    
    