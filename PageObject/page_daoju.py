# -*- coding: UTF-8 -*-
# @Time     :2020/9/15 16:44
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import time
import os
from selenium import webdriver
from Locators.daoju_locator import DaoJu_Locator as djl
from Common.handle_config import conf
from Base.base import BasePage
from Common.handle_picture import Handle_Picture
from Common.handle_path import DataPath

pic_dir = os.path.join(DataPath, 'pic')
target_pic = os.path.join(pic_dir, conf.get('daoju', 'target_pic'))
template_pic = os.path.join(pic_dir, conf.get('daoju', 'template_pic'))


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

    def silder_running(self):
        self.wait_frame_switch(djl.pic_iframe, '安全验证Iframe切换')
        target = self.get_attr(djl.target_bg, 'src', '获取背景图片url')
        template = self.get_attr(djl.template, 'src', '获取缺口图片url')
        # 下载背景图片和缺口图片
        target_path = Handle_Picture().download_pic(target, target_pic)
        template_path = Handle_Picture().download_pic(template, template_pic)
        # 获取缺口图片移动的最佳距离
        move_distance = Handle_Picture().find_picture(target_path, template_path)
        self.click_holding(djl.drag_slider, '点击并按住滑块')
        self.move_ele(djl.drag_slider, move_distance, 0, '按住并拖拽滑块')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = conf.get('daoju', 'url')
    daoju_page = DaoJu_Page(driver, url)
    daoju_page.daoju_login('1632577437', 'rao1632577437y')
    time.sleep(0.5)
    daoju_page.silder_running()
    time.sleep(10)
    driver.quit()
