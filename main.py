# Import du framework
import json
from fastapi import FastAPI
from firebase_admin import credentials
import pyrebase 
import routers.router_todo
import routers.router_auth 
from documentation.documentation import apidescription


app = FastAPI(description=apidescription)



# Router dédié aux Tasks
app.include_router(routers.router_todo.router)

app.include_router(routers.router_auth.router)
