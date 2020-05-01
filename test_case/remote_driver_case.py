# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium.webdriver.common.by import By

from config.basic_config import USERNAME, PASSWORD
from pages.house_login_page import HouseLoginPage
from pages.houses_info_page import HousesInfoPage
from utils.browser_engine import browser_engine
from config import logging_setting
from pages.houses_list_page import HousesListPage


class RemoteDriverCase(object):
    """远程浏览器测试用例"""
    logger = logging_setting.get_logger()

    def __init__(self):
        driver_dict = browser_engine.init_remote_driver()
        self.driver = driver_dict["linux"]

    def save_info(self):
        """
        保存房屋费用信息
        :return: 布尔值 True or False
        """
        self.logger.debug("远程浏览器测试用例开始执行~~")
        # 登陆
        houses_login_page = HouseLoginPage(self.driver)
        houses_login_page.get_login_page(USERNAME, PASSWORD)
        # 获取筛选后的房屋列表
        houses_list_page = HousesListPage(self.driver)
        houses_list_page.get_houses_list_driver("exchange", "深圳", "租房")

        rent_type_locator = (By.LINK_TEXT, "合租")
        price_range_locator = (By.LINK_TEXT, "1000-1500元")
        newest_locator = (By.LINK_TEXT, "最新上架")
        houses_list_page.get_selector_page([rent_type_locator, price_range_locator, newest_locator])
        self.logger.debug("得到筛选后的页面~~")

        houses_locator = (By.XPATH, "//div[@class='content__list']//div[1]//a[1]//img[1]")
        driver = houses_list_page.get_houses_info_page(houses_locator)
        self.logger.info("当前房屋信息的 url 地址是：{}".format(driver.current_url))
        # 保存房屋费用信息到数据库中
        try:
            houses_info = HousesInfoPage(driver)
            houses_info.save_product_info()
            self.logger.info("保存商品信息成功~")
            return True
        except:
            return False
        finally:
            # 关闭浏览器
            time.sleep(3)
            driver.quit()


RemoteDriver = RemoteDriverCase()
