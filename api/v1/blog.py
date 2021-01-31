#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: blog.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
博客前端，游客可见
"""

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
import db as models
from core import deps
from schemas import Response200, Response400
from schemas.review import ReviewCreate

blog_router = APIRouter(tags=["前台"])


# 文章相关API
@blog_router.get("/posts", name="分页文章列表", response_model=Response200)
async def get_posts(limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    total = db.query(func.count(models.Post.id)).scalar()
    posts = db.query(models.Post, models.Category).filter(models.Post.category_id == models.Category.id)\
        .order_by(models.Post.create_at.desc()).offset((page - 1) * 2).limit(limit).all()
    # posts = db.query(models.Post).order_by(models.Post.create_at.desc()).offset((page - 1) * 2).limit(limit).all()
    return Response200(data={"total": total, "posts": posts})


@blog_router.get("/posts/{post_id}", name="文章详情")
async def get_post(post_id: int, db: Session = Depends(deps.get_db)):
    # 连接查询返回分类名称
    post_obj = db.query(models.Post).get(post_id)
    post_obj.reading += 1
    db.commit()
    db.refresh(post_obj)
    post = db.query(models.Post, models.Category).filter(models.Post.category_id == models.Category.id).filter(
        models.Post.id == post_id
    ).first()
    return Response200(data={"post": post})


# 分类相关API
@blog_router.get("/sorts", name="分类列表")
async def get_sorts(limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    total = db.query(func.count(models.Category.id)).scalar()
    category = db.query(models.Category).order_by(models.Category.create_at.desc()).offset((page - 1) * 2).limit(
        limit).all()
    return Response200(data={"total": total, "category": category})


@blog_router.get("/sorts/{sort_id}/posts", name="分类文章列表")
async def get_sort_posts(sort_id: int, limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    total = 0
    if db.query(models.Category).get(sort_id):
        posts = db.query(models.Category, models.Post).filter(models.Category.id == models.Post.category_id).\
            filter_by(id=sort_id).order_by(models.Post.create_at.desc()).offset(
            (page - 1) * 2).limit(limit).all()
        total = len(posts)
    return Response200(data={"total": total, "posts": posts})


# 评论相关API
@blog_router.get("/reviews/{post_id}", name="评论列表")
async def get_reviews(post_id: int, limit: int = 5, page: int = 10 ,db: Session = Depends(deps.get_db)):
    data = db.query(models.Review).filter_by(post_id=post_id).order_by(models.Post.create_at.desc()).offset((page - 1) * 2).limit(limit).all()
    return Response200(data=data)


@blog_router.post("/reviews/{post_id}", name="发表评论")
async def create_review(post_id: int, review: ReviewCreate, db: Session = Depends(deps.get_db)):
    if db.query(models.Post).get(post_id):
        review_obj = models.Review(**review.dict())
        db.add(review_obj)
        db.commit()
        db.refresh(review_obj)
        return Response200(data=review_obj)
    return Response400(msg="评论失败，文章不存在")


@blog_router.post("/reviews/{review_id}", name="回复评论")
async def create_child_review(review_id: int, review: ReviewCreate, db: Session = Depends(deps.get_db)):
    if db.query(models.Review).get(review_id):
        review_obj = models.Review(**review.dict())
        db.add(review_obj)
        db.commit()
        db.refresh(review_obj)
        return Response200(data=review_obj)
    return Response400(msg="回复失败,评论不存在")

# todo 部分接口可能需要连表查询一次性返回 如 文章详情考虑 需要返回文章详细(分类名称、评论列表)，暂不更新
