#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: links.py
@author: zy7y
@time: 2021/1/11
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
友链表
"""
from models import Base, Column, Integer, String


class Links(Base):
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(60), comment="名称")
    url = Column(String(100), comment="链接地址")
