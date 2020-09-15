# -*- coding: UTF-8 -*-
# @Time     :2020/9/15 16:13
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
from selenium.webdriver.common.by import By


class Locator_Login:
    # 取消浮框定位
    Floating_frame = (By.XPATH, '//*[@id="popClose"]')
    # 登录框iframe
    login_frame = (By.ID, 'sydlzc2019')
    # 登录类型定位
    login_type = (By.XPATH, "//*[@id='loginform']/div/div/div")
    # 用户名输入框定位
    input_username = (By.XPATH, "//input[@name='username']")
    # 密码输入框定位
    input_password = (By.XPATH, "//input[@id='password']")
    # 滑块定位
    slider = (By.XPATH, "//*[@id='verify_bar']/div")
    # 图片缺口定位
    gap = (By.XPATH, "//*[@id='verify-code']/div/div/div[2]")
    # 登录按钮定位
    login_btn = (By.XPATH, '//*[@id="submitBtn"]')
    # 登录退出按钮定位
    logout_btn = (By.XPATH, '//*[@id="zcdl_04_list"]/div/div/div[1]/div[3]/input')
