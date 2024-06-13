from pathlib import Path


from fastapi import FastAPI, Form, HTTPException
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

STATIC_PATH = Path(__file__).resolve().parent / "static"
TEMPLATE_PATH = Path(__file__).resolve().parent / "templates"

static = StaticFiles(directory=STATIC_PATH)
templates = Jinja2Templates(directory=TEMPLATE_PATH)

app.mount("/static", static, name="static")

#HOME
@app.get("/", response_class=RedirectResponse)
async def render_home():
   return RedirectResponse(url="/home", status_code=303)

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
   ativos = await FavoriteService.list_favorite()
   return templates.TemplateResponse("ativos.html", {"request": request, "users": users, "ativos": ativos})

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

#É UTILIZADO POST, POIS FORM SÓ EXECUTAM POST E GET.  
@app.post('/delete', description='Deletes a user from the database', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def user_delete(user_id: int = Form(...)):
    try:
        await UserService.delete_user(user_id)
        return RedirectResponse(url='/cadastro', status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post('/favorite/add', description='Adds a favorite to the user', response_class=RedirectResponse, responses={400:{'model': ErrorOutput}})
async def user_favorite_add(user_id: int = Form(...), symbol: str = Form(...)):
    try:
       await FavoriteService.add_favorite(user_id=user_id, symbol=symbol)
       return RedirectResponse(url="/ativos", status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))

@app.post('/favorite/remove', description='deletes a favorite from the database', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_remove(user_id:int = Form(...), fav_id: int = Form(...)):
    try:
       await FavoriteService.remove_favorite(user_id=user_id, fav_id=fav_id)
       return RedirectResponse(url="/ativos", status_code=303)
    except Exception as e:
       raise HTTPException(400, detail=str(e))  
    