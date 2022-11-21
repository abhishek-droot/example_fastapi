from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass 

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    #title: str
    #content: str
    #published: bool
    #created_at: datetime

    class Config:
        orm_mode = True

class PostOut(PostBase):
    post: Post
    votes: int


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config: 
        orm_mode = True

class Userlogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
