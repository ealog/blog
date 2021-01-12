#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: comment.py
@author: zy7y
@time: 2021/1/10
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
评论路由
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core import deps
import db as models
import schemas.comment

router = APIRouter()


@router.get("/comments", summary="获取所有评论列表", response_model=List[schemas.comment.Comment])
def get_comments(
        db: Session = Depends(deps.get_db)
):
    return db.query(models.Comment).all()


@router.post("/comment", summary="新增评论")
def add_comment(
        comment: schemas.comment.CommentBase,
        db: Session = Depends(deps.get_db)
):
    comment_obj = models.Comment(**comment.dict())
    db.add(comment_obj)
    db.commit()
    db.refresh(comment_obj)
    return comment_obj


@router.delete("/comment/{comment_id}", summary="删除评论")
def delete_comment(
        comment_id: int,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    result = db.query(comment_id).get(comment_id)
    if result:
        db.delete(result)
        db.commit()
        return {"detail": "删除成功!"}
    raise HTTPException(status_code=404, detail="评论不存在.")