#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: post.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
文章列表
"""
from datetime import datetime

from pydantic import BaseModel


class Post(BaseModel):
    title: str


class PostCreate(Post):
    body: str
    status: int = 1
    category_id: int


class PostUpdate(PostCreate):
    reading: int


class PostBase(PostCreate):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: int
    reading: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
