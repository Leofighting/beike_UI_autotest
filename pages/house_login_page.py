# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium.webdriver.common.by import By

from config import basic_config
from config.logging_setting import get_logger
from pages.base_page import BasePage


class HouseLoginPage(BasePage):
    """登陆页面"""
    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver, basic_config.START_URL)

    def get_login_page(self, username, password):
        """
        获取登录页面
        :param username: 用户名
        :param password: 密码
        :return: 返回 浏览器 driver
        """
        self.logger.info("用户 {} 正在登陆~".format(username))
        driver = self.open()
        login_button_element = (By.CLASS_NAME, "reg")
        change_type_element = (By.CLASS_NAME, "change_login_type")
        username_element = (By.CLASS_NAME, "phonenum_input")
        password_element = (By.CLASS_NAME, "password_input")
        submit_element = (By.CLASS_NAME, "confirm_btn ")
        # 点击首页登陆按钮
        login_button = self.find_element(*login_button_element)
        login_button.click()
        # 点击切换使用 账户密码 登陆
        change_type = self.find_element(*change_type_element)
        change_type.click()
        # 输入 用户名
        username_ele = self.find_element(*username_element)
        username_ele.send_keys(username)
        # 输入 密码
        password_ele = self.find_element(*password_element)
        password_ele.send_keys(password)
        # 点击登录按钮
        submit = self.find_element(*submit_element)
        time.sleep(1)
        submit.click()

        # 验证是否登陆成功
        self.check_login(username)

        # 切换句柄
        handles = driver.window_handles
        index_handle = driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                driver.close()
                driver.switch_to.window(handle)

        self._driver = driver
        return driver

    def check_login(self, username):
        """
        验证用户是否登陆成功
        :param username: 用户名
        :return:
        """
        quit_element = (By.LINK_TEXT, "退出")
        try:
            # 通过页面上是否有退出连接判断是否登陆成功
            quit_ele = self.find_element(*quit_element)
            if quit_ele:
                self.logger.info("用户 {} 登陆成功~".format(username))
        except:
            self.logger.info("用户 {} 登陆失败~".format(username))
