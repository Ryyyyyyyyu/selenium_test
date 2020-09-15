# -*- coding: UTF-8 -*-
# @Time     :2020/9/15 16:44
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
from selenium import webdriver

from Locators.daoju_locator import DaoJu_Locator as djl
from Common.handle_config import conf
from Base.base import BasePage


class DaoJu_Page(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.get_url(self.url)
        self.driver.implicitly_wait(10)

    def daoju_login(self, user, pwd):
        self.wait_frame_switch(djl.login_frame, '登录Iframe切换')
        self.wait_element_click(djl.login_link, '点击账号密码登录')
        self.send(djl.user, user, '用户名输入框')
        self.send(djl.password, pwd, '密码输入框定位')
        self.wait_element_click(djl.log_btn, '登录按钮')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = conf.get('daoju', 'url')
    daoju_page = DaoJu_Page(driver, url)
    daoju_page.daoju_login('1632577437', 'rao1632577437y')
    driver.quit()
