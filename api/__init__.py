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
蓝图模式，实际api管理
"""
from fastapi import FastAPI, Request
from tools.logger import logger
from starlette.middleware.cors import CORSMiddleware

from api.v1 import router
from core.config import setting


def create_app():
    app = FastAPI(title="个人博客API",
              description="""
              默认账号: admin  默认密码: 123456
              参考资料
              - 模型设计参考《Flask Web开发实战_入门、进阶与原理解析（李辉著 ）》BlueBlog项目
              - 工厂模式和日志代码参考: https://github.com/CoderCharm
              """)
    app.include_router(router)

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

    return app
