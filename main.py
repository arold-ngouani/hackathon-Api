from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import routers.auth
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(routers.auth.router)