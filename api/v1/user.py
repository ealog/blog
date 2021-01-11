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
关于用户模型的-路由处理
"""

from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import db as models
from core import deps, security
from core.security import create_access_token
import schemas.user

router = APIRouter()


@router.post("/login", summary="用户登录", response_model=schemas.user.UserToken)
def user_login(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=404, detail="用户名或密码错误")
    user.token_type = "bearer"
    user.access_token = create_access_token(user.id)
    return user


@router.post("/users", summary="注册", response_model=schemas.user.User)
def register_user(
        user: schemas.user.UserCreate,
        db: Session = Depends(deps.get_db)
):
    result = db.query(models.User).filter(user.username == models.User.username).first()
    if result:
        raise HTTPException(status_code=400, detail="用户已存在，请重试!")
    user_obj = models.User(
        username=user.username,
        password_hash=security.get_password_hash(user.password),
        is_super=user.is_super
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


@router.put("/users/", summary="个人信息修改", response_model=schemas.user.User)
def update_user(
        user: schemas.user.UserUpdate = Body(...),
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    user_up = db.query(models.User).filter(models.User.id == user_token.id)
    if user_up.update({"username": user.username, "password_hash": security.get_password_hash(user.password)}):
        db.commit()
        user = user_up.first()
        return user
