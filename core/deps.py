#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: deps.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
依赖文件
"""
from typing import Generator

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import db as models
from core.security import analysis_token
from db.session import SessionLocal

user_oauth = OAuth2PasswordBearer(
    tokenUrl="/login"
)


# 数据库连接
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# token检查
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(user_oauth)
) -> models.User:
    token_data = analysis_token(token)
    user = db.query(models.User).get(token_data.get("sub"))
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在.")
    return user


