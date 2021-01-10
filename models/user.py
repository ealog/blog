#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: user.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
用户模型
"""


from models import Base, Column, Integer, String, Boolean


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), comment="邮箱账号", nullable=False)
    password_hash = Column(String(128), comment="密码", nullable=False)
    is_super = Column(Boolean, default=False, comment="管理员")
