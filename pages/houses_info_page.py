# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.webdriver.common.by import By

from config import basic_config
from config.logging_setting import get_logger
from model.beike_model import House_Info
from pages.base_page import BasePage


class HousesInfoPage(BasePage):
    """房屋详细信息页面"""
    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver, basic_config.START_URL)

    def save_product_info(self):
        """
        保存房屋信息
        :return:
        """
        js = "window.scrollTo(0, 100)"
        self._driver.execute_script(js)
        # 定位到费用详情
        price_element = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[3]/div[3]/ul[1]/li[3]")
        self.find_element(*price_element).click()
        info_ele = (By.CLASS_NAME, "cost_content")
        info_elements = self.find_elements(*info_ele)

        result_list = []
        for info_element in info_elements:
            info_element_dict = self.__get_info_element_dict(info_element)
            result_list.append(info_element_dict)
        self.__save_info_to_mysql(result_list)

    def __get_info_element_dict(self, info_element):
        """
        获取元素定位信息字典
        :param info_element: 元素定位信息
        :return: 元素定位信息字典
        """

        # 房屋费用表标题
        price_part_element = (By.CLASS_NAME, "title_info")
        price_part = self.find_element(*price_part_element, element=info_element)
        # 房屋费用表第一行的值，作为字典的 key
        price_first_element = (By.CLASS_NAME, "table_title")
        price_first = self.find_element(*price_first_element, element=info_element)
        price_first_keys_element = (By.TAG_NAME, "li")
        price_first_keys = self.find_elements(*price_first_keys_element, element=price_first)
        # 房屋费用表第二行的值，作为字典的 value
        price_second_element = (By.CLASS_NAME, "table_content")
        price_second = self.find_element(*price_second_element, element=info_element)
        price_second_values_element = (By.TAG_NAME, "li")
        price_second_values = self.find_elements(*price_second_values_element, element=price_second)

        self.logger.debug("获取到所有的费用信息")

        key_and_value_dict = {}
        parts_dict = {}

        for i in range(len(price_first_keys)):
            price_key = price_first_keys[i].text.split("<span")[0]
            price_value = price_second_values[i].text
            key_and_value_dict[price_key] = price_value

        parts_dict[price_part.text] = key_and_value_dict

        return parts_dict

    @staticmethod
    def __save_info_to_mysql(info_list):
        """
        保存信息到数据库中
        :param info_list: 信息列表
        :return: 信息列表
        """
        houses = House_Info()
        for info in info_list:
            for key, value in info.items():
                houses.insert(["price_part", "price_info"], [str(key), str(value)])
