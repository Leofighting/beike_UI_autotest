# -*- coding:utf-8 -*-
__author__ = "leo"

import logging.config
import logging
import os


def get_logger(name="myAutoTest"):
    """启动日志系统"""
    config_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.conf")
    logging.config.fileConfig(config_log)
    logger = logging.getLogger(name)

    return logger
