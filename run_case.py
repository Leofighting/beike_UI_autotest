# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import time
import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

from test_case.local_driver_case import LocalDriver
from test_case.local_driver_no_gui_case import LocalDriverNoGui
from test_case.remote_driver_case import RemoteDriver
from test_case.remote_driver_no_gui_case import RemoteDriverNoGui
from test_case import thread_driver_case


class RunCase(unittest.TestCase):

    def test_local_driver(self):
        result = LocalDriver.save_info()
        self.assertTrue(result)

    def test_local_driver_no_gui(self):
        result = LocalDriverNoGui.save_info()
        self.assertTrue(result)

    def test_remote_driver(self):
        result = RemoteDriver.save_info()
        self.assertTrue(result)

    def test_remote_driver_no_gui(self):
        result = RemoteDriverNoGui.save_info()
        self.assertTrue(result)

    def test_thread_driver(self):
        result = thread_driver_case.thread_driver()
        self.assertIsNone(result)


if __name__ == '__main__':
    # 按需执行测试用例，利用 unittest 的容器
    suite = unittest.TestSuite()
    # 测试用例列表
    test_case_list = [RunCase("test_local_driver"), RunCase("test_local_driver_no_gui"),
                      RunCase("test_remote_driver"), RunCase("test_remote_driver_no_gui"),
                      RunCase("test_thread_driver")]
    # 测试多线程远程自动化用例
    # test_case_list = [RunCase("test_thread_driver")]
    # 将测试用例列表添加到容器中
    suite.addTests(test_case_list)
    # 生成测试报告：以时间戳定义报告名称
    file_path = os.getcwd() + "/report/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_time = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    html_file = file_path + file_time + "_report.html"

    with open(html_file, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="贝壳找房网 web 自动化测试", description="针对登陆页面以及商品详情页进行测试")
        runner.run(suite)
