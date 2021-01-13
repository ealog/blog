#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: config.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
配置文件
"""
import secrets
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """配置类"""

    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3

    # 跨域设置
    ORIGINS: List[str] = ["*", ]

    # 数据库url配置
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///db/blog.db"


setting = Settings()
