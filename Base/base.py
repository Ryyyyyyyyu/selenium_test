# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 18:02
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import os
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.handle_logger import log
from Common.handle_path import ReportPath


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def save_image(self, filename='未命名'):
        now = time.strftime('%Y-%m-%d_%H-%M-%S')
        image_dir = os.path.join(ReportPath, 'err_image')
        filepath = os.path.join(image_dir, '{}-{}.png'.format(now, filename))
        self.driver.save_screenshot(filename=filepath)
        log.debug('{}错误截图保存在{}'.format(filename, filepath))

    def get_url(self, url):
        return self.driver.get(url)

    def find_ele(self, locator, *args):
        """查找基础元素"""
        now = time.time()
        try:
            ele = self.driver.find_element(*locator)
            log.debug('通过{}定位，定位元素是{}'.format(*locator))
        except Exception as e:
            self.save_image(*args)
            log.error('通过{}定位{}失败'.format(*locator))
            log.exception(e)
            raise e
        else:
            last = time.time()
            log.debug('查找该元素耗时{}秒'.format(last - now))
            return ele

    def click_ele(self, locator, *args):
        """点击元素"""
        self.find_ele(locator, *args).click()

    def send(self, locator, value, *args):
        """在输入类型元素中填写文本"""
        self.find_ele(locator, *args).send_keys(value)

    def switch_frame(self, locator):
        self.driver.switch_to.frame(self.find_ele(locator))

    def clear(self, locator):
        self.find_ele(locator).click()

    def act(self):
        return ActionChains(self.driver)

    def click_holding(self, locator, *args):
        return self.act().click_and_hold(self.find_ele(locator, *args)).perform()

    def drag_drop(self, locator1, locator2, *args):
        return self.act().drag_and_drop(self.find_ele(locator1, args[0]), self.find_ele(locator2, args[1])).perform()

    def wait_element_visibility(self, locator, *args, timeout=10, poll_frequency=0.2):
        now = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            log.debug('通过{}定位，定位元素是{}'.format(*locator))
        except Exception as e:
            self.save_image(*args)
            log.error('通过{}定位{}失败'.format(*locator))
            log.exception(e)
            raise e
        else:
            last = time.time()
            log.debug('查找该元素耗时{}秒'.format(last - now))
            return ele

    def wait_element_click(self, locator, *args, timeout=10, poll_frequency=0.2):
        now = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator)).click()
            log.debug('通过{}定位，定位元素是{}'.format(*locator))
        except Exception as e:
            self.save_image(*args)
            log.error('通过{}定位{}失败'.format(*locator))
            log.exception(e)
            raise e
        else:
            last = time.time()
            log.debug('查找该元素耗时{}秒'.format(last - now))
            return ele

    def wait_frame_switch(self, locator, *args, timeout=10, poll_frequency=0.2):
        now = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
            log.debug('通过{}定位，定位元素是{}'.format(*locator))
        except Exception as e:
            self.save_image(*args)
            log.error('通过{}定位{}失败'.format(*locator))
            log.exception(e)
            raise e
        else:
            last = time.time()
            log.debug('查找该元素耗时{}秒'.format(last - now))
            return ele


if __name__ == '__main__':
    from selenium import webdriver

    driver1 = webdriver.Chrome()
    url = 'https://www.baidu.com/'
    driver1.get(url)
    s = BasePage(driver1)
    loc1 = (By.ID, 'kw1')
    i = s.wait_element_visibility(loc1, '输入框', timeout=5, poll_frequency=0.1)
    i.send_keys('python')
    loc2 = (By.ID, 'su')
    s.click_ele(loc2, '点击')
    time.sleep(5)
    s.driver.quit()
