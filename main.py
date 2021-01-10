#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: main.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
启动文件
"""

from fastapi import FastAPI

from api.v1 import user, category, post

app = FastAPI()
app.include_router(user.router, tags=["用户管理"])
app.include_router(category.router, tags=["分类管理"])
app.include_router(post.router, tags=["文章管理"])


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True, debug=True)