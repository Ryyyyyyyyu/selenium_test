# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 18:02
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import os
import time

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
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
        """保存错误截图"""
        now = time.strftime('%Y-%m-%d_%H-%M-%S')
        image_dir = os.path.join(ReportPath, 'err_image')
        filepath = os.path.join(image_dir, '{}-{}.png'.format(now, filename))
        self.driver.save_screenshot(filename=filepath)
        log.debug('{}错误截图保存在{}'.format(filename, filepath))

    def get_url(self, url):
        """获取访问url地址"""
        log.debug('获取访问url地址{}'.format(url))
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
        log.debug('开始点击{}元素'.format(locator))
        self.find_ele(locator, *args).click()

    def send(self, locator, value, *args):
        """在输入类型元素中填写文本"""
        ele = self.find_ele(locator, *args)
        ele.clear()
        ele.send_keys(value)

    def switch_frame(self, locator):
        """切换iframe"""
        return self.driver.switch_to.frame(locator)

    def switch_parent_frame(self):
        """切换到上层iframe"""
        return self.driver.switch_to.parent_frame()

    def switch_to_default(self):
        """切换到第一层iframe"""
        return self.driver.switch_to.default_content()

    def clear(self, locator):
        """清除输入框内容"""
        self.find_ele(locator).clear()

    def get_text(self, locator):
        """获取元素文本信息"""
        return self.find_ele(locator).text

    def get_attr(self, locator, name, *args):
        return self.find_ele(locator, *args).get_attribute(name)

    def js(self, script):
        """通过js语句操作"""
        self.driver.execute_script(script)

    def act(self):
        """创建鼠标操作对象"""
        return ActionChains(self.driver)

    def click_holding(self, locator, *args):
        """模拟鼠标点击某一元素并按住不松开"""
        return self.act().click_and_hold(self.find_ele(locator, *args)).perform()

    def move_mouse(self, xmove, ymove):
        """移动鼠标"""
        return self.act().move_by_offset(xmove, ymove).perform()

    def move_ele(self, locator, xoffset, yoffset, *args):
        """按住某一元素拖拽至偏移x,y的位置并释放鼠标"""
        return self.act().drag_and_drop_by_offset(self.find_ele(locator, *args), xoffset, yoffset).perform()

    def drag_drop(self, locator1, locator2, *args):
        """模拟鼠标将元素1拖拽到元素2的位置"""
        return self.act().drag_and_drop(self.find_ele(locator1, args[0]), self.find_ele(locator2, args[1])).perform()

    def alert_click(self, timeout=10, poll_frequency=0.1):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            return alert
        except TimeoutException as e:
            log.info('{}秒还没有出现弹框'.format(timeout))
            log.exception(e)

    def wait_element_visibility(self, locator, *args, timeout=10, poll_frequency=0.2):
        """显示等待元素可见"""
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
        """显示等待元素可点击"""
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
        """显示等待判断iframe是否可切入，若可以则切换到iframe"""
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
    b = BasePage(driver1)
    loc1 = (By.ID, 'kw1')
    i = b.wait_element_visibility(loc1, '输入框', timeout=5, poll_frequency=0.1)
    i.send_keys('python')
    loc2 = (By.ID, 'su')
    b.click_ele(loc2, '点击')
    time.sleep(5)
    b.driver.quit()
