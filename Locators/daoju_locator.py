# -*- coding: UTF-8 -*-
# @Time     :2020/9/15 18:19
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
from selenium.webdriver.common.by import By


class DaoJu_Locator:
    # 登录框iframe
    login_frame = (By.ID, 'loginIframe')
    # 点击账号密码登录
    login_link = (By.XPATH, '//*[@id="switcher_plogin"]')
    # 用户名输入框定位
    user = (By.ID, 'u')
    # 密码输入框定位
    password = (By.ID, 'p')
    # 登录按钮
    log_btn = (By.XPATH, '//*[@id="login_button"]')
    # 安全验证的iframe
    pic_iframe = (By.ID, 'tcaptcha_iframe')
    # 背景图片
    target_bg = (By.ID, 'slideBg')
    # 缺口滑块
    template = (By.ID, 'slideBlock')
    # 滑块
    drag_slider = (By.ID, 'tcaptcha_drag_thumb')
