from typing import Optional, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models, database, config
from app.routers import auth, posts, users, vote


## Not needed after alembic
# database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = [
    "https://www.google.com",
    "https://www.youtube.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World!"}


app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(vote.router)