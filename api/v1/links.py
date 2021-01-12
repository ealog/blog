#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: links.py
@author: zy7y
@time: 2021/1/12
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
友链
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import db as models
import schemas.links
from core import deps

router = APIRouter()


@router.get("/links", summary="友链列表", response_model=List[schemas.links.Links])
def get_links(
        db: Session = Depends(deps.get_db)
):
    return db.query(models.Links).all()


@router.post("/link", summary="新增友链", response_model=schemas.links.Links)
def add_link(
        link: schemas.links.LinksBase,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    link_obj = models.Links(**link.dict())
    db.add(link_obj)
    db.commit()
    db.refresh(link_obj)
    return link_obj


@router.put("/link", summary="修改友链", response_model=schemas.links.Links)
def update_link(
        link_id: int,
        link: schemas.links.LinksBase,
        db: Session = Depends(deps.get_db),
        user_token: models.User = Depends(deps.get_current_user)
):
    link_obj = db.query(models.Links).filter(models.Links.id == link_id)
    if link_obj.update({"name": link.name, "url": link.url}):
        db.commit()
        return link_obj.first()
    raise HTTPException(status_code=404, detail="友链不存在.")
