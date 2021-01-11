#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: post.py
@author: zy7y
@time: 2021/1/10
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
文章路由
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas.post
from core import deps
import db as models

router = APIRouter()


@router.post("/post", summary="新增文章", response_model=schemas.post.Post)
def post_add(
        post: schemas.post.PostCreate,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    if not db.query(models.Category).get(post.category_id):
        raise HTTPException(status_code=404, detail="分类不存在.")
    post_obj = models.Post(**post.dict())
    post_obj.user_id = user_token.id
    db.add(post_obj)
    db.commit()
    db.refresh(post_obj)
    return post_obj


@router.get("/posts", summary="文章列表", response_model=List[schemas.post.Post])
def post_list(
        db: Session = Depends(deps.get_db),
):
    return db.query(models.Post).all()


@router.get("/posts/{post_id}", summary="文章详情", response_model=schemas.post.Post)
def post_info(
        post_id: int,
        db: Session = Depends(deps.get_db),
):
    result = db.query(models.Post).get(post_id)
    if not result:
        raise HTTPException(status_code=404, detail="文章不存在.")
    return result


@router.put("/posts/{post_id}", summary="文章修改")
def post_update(
        post: schemas.post.PostCreate,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    pass