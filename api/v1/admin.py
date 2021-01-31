#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: admin.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
管理内容的api
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import deps
from core.security import get_password_hash
from schemas import Response200, Response400
from schemas.admin import AdminUpdate
from schemas.category import CategoryCreate
from schemas.post import PostCreate, PostUpdate
import db as models
from typing import Union

admin_router = APIRouter(prefix="/admin", tags=["后台"], dependencies=[Depends(deps.get_current_user)])


# 文章管理API
@admin_router.post("/posts", name="新增文章", response_model=Union[Response200, Response400])
async def create_post(post: PostCreate, db: Session = Depends(deps.get_db)):
    """文章创建"""
    if db.query(models.Category).get(post.category_id):
        post_obj = models.Post(**post.dict())
        db.add(post_obj)
        db.commit()
        db.refresh(post_obj)
        return Response200(data={"post": post_obj})
    else:
        return Response400(msg="新增失败,分类不存在")


@admin_router.put("/posts/{post_id}", name="更新文章", response_model=Union[Response200, Response400])
async def update_post(post_id: int, post: PostUpdate, db: Session = Depends(deps.get_db)):
    """文章更新"""
    post_obj = db.query(models.Post).filter_by(id=post_id)
    if post_obj:
        post_obj.update({
            "title": post.title,
            "body": post.body,
            "status": post.status,
            "category_id": post.category_id
        })
        db.commit()
        return Response200(data={"post": post_obj.first()})
    return Response400(msg="更新失败,文章不存在")


@admin_router.delete("/posts/{post_id}", name="删除文章", response_model=Union[Response200, Response400])
async def delete_post(post_id: int, db: Session = Depends(deps.get_db)):
    """文章删除"""
    post_obj = db.query(models.Post).get(post_id)
    if post_obj:
        db.delete(post_obj)
        db.commit()
        return Response200(data={"post": post_obj})
    return Response400(msg="删除失败,文章不存在")


# 分类管理API
@admin_router.post("/sorts", name="新增分类", response_model=Union[Response200, Response400])
async def create_sort(
        category: CategoryCreate,
        db: Session = Depends(deps.get_db)):
    """分类创建"""
    category_result = db.query(models.Category).filter_by(name=category.name).first()

    if category_result:
        return Response400(msg="新增失败,分类已存在")
    category_obj = models.Category(
        name=category.name
    )
    db.add(category_obj)
    db.commit()
    db.refresh(category_obj)
    return Response200(data={"category": category_obj})


@admin_router.put("/sorts/{sort_id}", name="更新分类", response_model=Union[Response200, Response400])
async def update_sort(sort_id: int, category: CategoryCreate, db: Session = Depends(deps.get_db)):
    """分类更新"""
    category_obj = db.query(models.Category).filter_by(id=sort_id)
    if category_obj:
        category_obj.update({
            "name": category.name
        })
        db.commit()
        return Response200(data={"category": category_obj.first()})
    return Response400(msg="修改失败,分类不存在")


@admin_router.delete("/sorts/{sort_id}", name="删除分类", response_model=Union[Response200, Response400])
async def delete_sort(sort_id: int, db: Session = Depends(deps.get_db)):
    """分类删除"""
    category_obj = db.query(models.Category).get(sort_id)
    if category_obj:
        db.delete(category_obj)
        db.commit()
        return Response200(data=category_obj)
    return Response400(msg="删除失败,分类不存在")


# 评论管理API
@admin_router.delete("/reviews/{review_id}", name="删除评论", response_model=Union[Response200, Response400])
async def delete_review(review_id: int, db: Session = Depends(deps.get_db)):
    """删除评论"""
    review_obj = db.query(models.Review).get(review_id)
    if review_obj:
        db.delete(review_obj)
        db.commit()
        return Response200(data=review_obj)
    return Response400(msg="删除失败,评论不存在")


# 资料设置API
@admin_router.put("/info", name="博客资料修改", response_model=Union[Response200, Response400])
async def update_info(site: AdminUpdate, db: Session = Depends(deps.get_db)):
    """博客资料修改"""
    site_obj = db.query(models.Admin).filter_by(id=1)
    site_obj.update({
        "about": site.about,
        "blog_sub_title": site.blog_sub_title,
        "password_hash": get_password_hash(site.password),
        "username": site.username,
        "name": site.name,
        "blog_title": site.blog_title,
    })
    db.commit()
    return Response200(data=site)

