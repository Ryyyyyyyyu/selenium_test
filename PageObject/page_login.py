# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 17:53
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
from selenium.webdriver.common.by import By
from Common.handle_logger import log
from Base.base import BasePage


class Login_Page(BasePage):

    def login(self, username, password):
        self.click_ele((By.XPATH, '//*[@id="popClose"]'), '取消浮框')
        self.wait_frame_switch((By.ID, 'sydlzc2019'))
        self.wait_element_click((By.XPATH, "//*[@id='loginform']/div/div/div"), '选择登录类型')
        username_ele = (By.XPATH, "//input[@name='username']")
        password_ele = (By.XPATH, "//input[@id='password']")
        self.clear(username_ele)
        self.send(username_ele, username, '定位用户名输入框')
        log.debug('用户名输入完成')
        self.clear(password_ele)
        self.send(password_ele, password, '定位密码输入框')
        log.debug('密码输入完成')

    def silde_runing(self):
        slider = (By.XPATH, "//*[@id='verify_bar']/div")
        self.click_holding((By.XPATH, "//*[@id='verify_bar']/div"), '滑块定位')
        gap = (By.XPATH, "//*[@id='verify-code']/div/div/div[2]")
        self.drag_drop(slider, gap, '滑块定位', '图片缺口定位')

    def click_login(self):
        self.wait_element_click((By.XPATH, '//*[@id="submitBtn"]'), '登录按钮定位')

    def click_logout(self):
        self.wait_element_click((By.XPATH, '//*[@id="zcdl_04_list"]/div/div/div[1]/div[3]/input'), '退出按钮定位')
