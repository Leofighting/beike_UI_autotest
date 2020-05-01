# -*- coding:utf-8 -*-
__author__ = "leo"

from orm.field import Field
from orm.orm import Model


class House_Info(Model):
    """创建数据库表"""
    price_part = Field("price_part", "varchar(255")
    price_info = Field("price_info", "text")
