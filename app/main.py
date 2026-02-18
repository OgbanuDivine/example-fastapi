from fastapi import FastAPI  #Response, status, HTTPException, Depends
from . import models         # schemas, utils
from .database import engine   # get_db
from .routers import post, user, auth, vote
from .config import settings
models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://www.google.com",
            "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Requests comesin with a guest method and the url is '/'

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hell Yeahhhh"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return{"data": "successful"}

# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# from sqlalchemy.orm import Session
