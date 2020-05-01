# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import basic_config


class BasePage(object):
    """基础页面"""

    def __init__(self, driver, url):
        """
        构造方法
        :param driver: 具体启动哪个浏览器
        :param url: 目标 url
        """
        self._driver = driver
        self._url = url

    def open(self):
        """
        打开指定的网页
        :return: 浏览器的 driver
        """
        self._driver.get(url=self._url)
        return self._driver

    def find_element(self, *locator, element=None,
                     timeout=None, wait_time="visibility",
                     when_failed_close_browser=True):
        """
        查找页面元素，支持以 driver 或 element 的方式进行元素查找
        :param locator: 元素定位方式，格式：(By.ID, "element_id")
        :param element: 默认为None, 如果有值，则是一个页面元素，将会在此元素之上查找子元素
        :param timeout: 默认为None, 取配置文件中的时间配置值
        :param wait_time: 等待类型，支持两种等待方式：元素可见等待，元素存在等待
        :param when_failed_close_browser: 当元素定位时，浏览器是否关闭
        :return: 返回定位元素
        """
        if element is not None:
            return self._init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))

        try:
            if wait_time == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_element_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式：{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式：{}".format(locator))

    def find_elements(self, *locator, element=None,
                      timeout=None, wait_time="visibility",
                      when_failed_close_browser=True):
        """
        查找页面的多个元素，支持以 driver 或 element 的方式进行元素查找
        :param locator: 元素定位方式，格式：(By.ID, "element_id")
        :param element: 默认为None, 如果有值，则是一个页面元素，将会在此元素之上查找子元素
        :param timeout: 默认为None, 取配置文件中的时间配置值
        :param wait_time: 等待类型，支持两种等待方式：元素可见等待，元素存在等待
        :param when_failed_close_browser: 当元素定位时，浏览器是否关闭
        :return: 返回多个定位元素
        """
        if element is not None:
            return element.find_elements(*locator)

        try:
            if wait_time == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式：{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式：{}".format(locator))

    def _init_wait(self, timeout=None):
        """
        时间等待
        :param timeout: 时间
        :return: 元素查找结果
        """
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=basic_config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
