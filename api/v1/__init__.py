#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: __init__.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
汇总路由
"""


from fastapi import APIRouter

from api.v1.admin import admin_router
from api.v1.auth import auth_router
from api.v1.blog import blog_router

router = APIRouter(prefix="/v1")


router.include_router(blog_router)
router.include_router(auth_router)
router.include_router(admin_router)
