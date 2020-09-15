# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 17:53
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
from selenium.webdriver.common.by import By
from Common.handle_logger import log
from Base.base import BasePage
from Locators.login_locator import Locator_Login as locl


class Login_Page(BasePage):

    def login(self, username, password):
        self.click_ele(locl.Floating_frame, '取消浮框')
        self.wait_frame_switch(locl.login_frame)
        self.wait_element_click(locl.login_type, '选择登录类型')
        self.clear(locl.input_username)
        self.send(locl.input_username, username, '定位用户名输入框')
        log.debug('用户名输入完成')
        self.clear(locl.input_password)
        self.send(locl.input_password, password, '定位密码输入框')
        log.debug('密码输入完成')

    def silde_runing(self):
        self.click_holding(locl.slider, '滑块定位')
        self.drag_drop(locl.slider, locl.gap, '滑块定位', '图片缺口定位')

    def click_login(self):
        self.wait_element_click(locl.login_btn, '登录按钮定位')

    def click_logout(self):
        self.wait_element_click(locl.logout_btn, '退出按钮定位')
