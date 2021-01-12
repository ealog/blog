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
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    body: str
    is_show: bool = True
    category_id: int


class PostList(PostBase):
    id: int
    create_at: datetime
    update_at: datetime


class Post(PostCreate):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    class Config:
        orm_mode = True
