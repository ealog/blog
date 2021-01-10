#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: user.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:

"""
from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username: Optional[EmailStr] = None
    is_super: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# 数据库操作

class UserInDBBase(UserBase):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


class UserToken(UserInDBBase):
    """通过API返回的属性"""
    access_token: str
    token_type: str


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    """写入数据库时用的属性"""
    password_hash: str
