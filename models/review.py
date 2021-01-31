#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: review.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
评论模型
"""
from models import Base, Column, Integer, Text, String


class Review(Base):
    id = Column(Integer, index=True, primary_key=True)
    author = Column(String(30), comment="昵称")
    pid = Column(Integer, default=id, comment="父级评论ID")
    post_id = Column(Integer, comment="评论的文章")
    content = Column(Text, comment="评论内容")
