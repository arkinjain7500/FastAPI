from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str


# class ShowBlog(Blog):
#     creator: ShowUser


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    # password: str
    blogs: List[Blog] = []
    # password: str

class ShowBlog(Blog):
    creator: ShowUser

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None