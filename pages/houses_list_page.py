# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.webdriver.common.by import By

from config import basic_config
from config.logging_setting import get_logger
from pages.base_page import BasePage


class HousesListPage(BasePage):
    """
    房屋列表页面
    """
    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver, basic_config.START_URL)

    def get_houses_list_driver(self, first_list_name, second_list_name, third_list_name):
        """
        获取房屋信息列表
        :param first_list_name: 第一个元素的关键字
        :param second_list_name: 第二个元素的关键字
        :param third_list_name: 第三个元素的关键字
        :return: 浏览器的 driver
        """
        driver = self.open()
        first_element = (By.CLASS_NAME, first_list_name)
        second_element = (By.LINK_TEXT, second_list_name)
        third_element = (By.LINK_TEXT, third_list_name)

        first = self.find_element(*first_element)
        first.click()

        second = self.find_element(*second_element)
        second.click()

        third = self.find_element(*third_element)
        third.click()

        # 切换句柄
        handles = driver.window_handles
        index_handle = driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                driver.close()
                driver.switch_to.window(handle)

        self.logger.info("获取到页面：" + second_list_name)
        self.logger.info("当前 url 是：" + driver.current_url)

        self._driver = driver
        return driver

    def get_selector_page(self, selector_condition_list):
        """
        获取筛选后的页面
        :param selector_condition_list: 筛选条件列表，格式：[(By.ID, "id_value"), (By.NAME, "name_value")]
        :return:
        """
        for condition in selector_condition_list:
            element = self.find_element(*condition)
            element.click()

    def get_houses_info_page(self, selector_condition):
        """
        获取房屋信息页面
        :param selector_condition: 具体商品的筛选条件，格式：(By.ID, "id_value")
        :return: 页面的 driver
        """
        self.find_element(*selector_condition).click()

        # 切换句柄
        handles = self._driver.window_handles
        index_handle = self._driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                self._driver.close()
                self._driver.switch_to.window(handle)

        return self._driver
