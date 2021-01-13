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

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from api.v1 import user, category, post, links, options, comment
from core.config import setting
from tools.logger import logger

app = FastAPI(title="Blog接口文档")

# 设置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 自定义访问日志中间件
@app.middleware("http")
async def logger_request(request: Request, call_next):
    # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
    logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers.get('user-agent')}"
                f"\nIP:{request.client.host}")
    response = await call_next(request)
    return response


app.include_router(user.router, tags=["用户管理"])
app.include_router(category.router, tags=["分类管理"])
app.include_router(post.router, tags=["文章管理"])
app.include_router(comment.router, tags=["评论管理"])
app.include_router(links.router, tags=["友链管理"])
app.include_router(options.router, tags=["设置管理"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, debug=True)
