from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user , auth, vote
from .config import settings
# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     database_password: str = "localhost"
#     database_username: str = "postgres"
#     secret_key: str = "234ui2340892348"

# settings = Settings()

print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# request Get method url: "/"
@app.get("/")
def root():
    return {"message":"Hello world pushing out to ubuntu"}
