#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: options.py
@author: zy7y
@time: 2021/1/11
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
设置表
"""
from models import Base, Column, Integer, String, Text


class Options(Base):
    id = Column(Integer, index=True, primary_key=True)
    blog_title = Column(String(50), comment="博客标题")
    blog_sub_title = Column(String(100), comment="博客副标题")
    about = Column(Text, comment="关于")