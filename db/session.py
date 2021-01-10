#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: session.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
连接数据库
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import setting

engine = create_engine(setting.SQLALCHEMY_DATABASE_URI,  connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
