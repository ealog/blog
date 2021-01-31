#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: category.py
@author: zy7y
@time: 2021/1/10
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
分类表
"""
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class Category(BaseModel):
    """新增/修改都使用这个模型"""
    name: str


class CategoryCreate(Category):
    pass


class CategoryBase(Category):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
