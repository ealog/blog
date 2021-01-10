#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: security.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
token生成
"""
from datetime import datetime, timedelta
from typing import Any, Union

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import ValidationError

from core.config import setting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """使用哈希算法加密密码"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码与hash密码"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
        subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    token生成的方法
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    # 加密生成token
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt


def analysis_token(token: str) -> dict:
    """解密token"""
    try:
        payload = jwt.decode(
            token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM]
        )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=403, detail="token无效")
    return payload
