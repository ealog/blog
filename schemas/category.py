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

from typing import Optional

from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    name: str


# Properties to receive via API on creation
class CategoryCreate(CategoryBase):
    pass


# Properties to receive via API on update
class CategoryUpdate(CategoryBase):
    name: str


# 数据库操作

class CategoryInDBBase(CategoryBase):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Category(CategoryInDBBase):
    pass

