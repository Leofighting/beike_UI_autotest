# -*- coding:utf-8 -*-
__author__ = "leo"

import pymysql
from DBUtils.PooledDB import PooledDB

from config.mysql_config import set_mysql_config


def create_pool():
    """创建数据库连接池"""
    db_config = set_mysql_config("dev")
    return PooledDB(pymysql, 5,
                    host=db_config["host"],
                    user=db_config["user"],
                    password=db_config["password"],
                    database=db_config["database"],
                    port=db_config["port"],
                    charset=db_config["charset"]).connection()
