#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: options.py
@author: zy7y
@time: 2021/1/12
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
设置
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import deps
import db as models
import schemas.options

router = APIRouter()


@router.get("/options", summary="获取平台设置项", response_model=schemas.options.Options)
def get_options(
        db: Session = Depends(deps.get_db)
):
    return db.query(models.Options).first()


@router.put("/options", summary="修改配置项", response_model=schemas.options.Options)
def update_options(
        options: schemas.options.OptionsBase,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    result = db.query(models.Options).filter(models.Options.id == 1)
    if result.update({
        "blog_title": options.blog_title,
        "blog_sub_title": options.blog_sub_title,
        "about": options.about
    }):
        db.commit()
        return result.first()

