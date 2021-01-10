#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: comment.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
评论模型
"""
from models import Base, Column, Integer, Text


class Comment(Base):
    id = Column(Integer, index=True, primary_key=True)
    pid = Column(Integer, default=0, comment="父级评论")
    post_id = Column(Integer, comment="评论的文章")
    content = Column(Text, comment="评论内容")