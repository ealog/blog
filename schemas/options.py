#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: options.py
@author: zy7y
@time: 2021/1/12
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
设置
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class OptionsBase(BaseModel):
    blog_title: str
    blog_sub_title: str
    about: str


# Additional properties to return via API
class Options(OptionsBase):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True