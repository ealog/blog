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
文章模型
"""
from models import Base, Column, Integer, String, Text, Boolean


class Post(Base):
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(100), comment="文章标题")
    body = Column(Text, comment="文章内容")
    is_show = Column(Boolean, default=True, comment="是否显示")
    category_id = Column(Integer, comment="分类")