# -*- coding:utf-8 -*-
__author__ = "leo"


def set_mysql_config(env):
    """配置数据库参数"""
    if env == "dev":
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "123456",
            "database": "python_ui",
            "port": 3306,
            "charset": "utf8"
        }
    if env == "pro":
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "123456",
            "database": "python_ui",
            "port": 3306,
            "charset": "utf8"
        }

    return db_config
