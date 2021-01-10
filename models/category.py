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
from models import Base, Column, Integer, String


class Category(Base):
    """分类表"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), comment="分类名称")
    user_id = Column(Integer, index=True, comment="所属用户")
