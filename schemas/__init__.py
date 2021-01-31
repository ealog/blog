#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: response.py
@author: zy7y
@time: 2021/1/30
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
定义response响应模型
"""
from typing import Any

from pydantic import BaseModel


class ResponseBase(BaseModel):
    data: Any = None


class Response200(ResponseBase):
    code = 200
    msg = "操作成功."


class Response400(ResponseBase):
    code = 400
    msg = "请求错误."
