#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: links.py
@author: zy7y
@time: 2021/1/12
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
友链
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# 创建/修改的基类
class LinksBase(BaseModel):
    name: str
    url: str


# 数据库查询出来的模型类
class Links(LinksBase):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

