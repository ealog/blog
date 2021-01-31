#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: admin.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
管理员模型
"""
from models import Base, Column, Integer, Text, String


class Admin(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), comment="账号")
    password_hash = Column(String(128), comment="密码")
    blog_title = Column(String(60), comment="博客标题")
    blog_sub_title = Column(String(100), comment="博客子标题")
    name = Column(String(30), comment="作者名称")
    about = Column(Text, comment="关于")


