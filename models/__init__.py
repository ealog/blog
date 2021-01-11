#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: __init__.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
数据库表(模型类)定义的包
"""
from datetime import datetime

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy import *

"""指定为SqlAlchemy的Base类"""


@as_declarative()
class Base:
    id: int
    __name__: str
    create_at: DateTime = Column(DateTime, default=datetime.now, comment="创建时间")
    update_at: DateTime = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
