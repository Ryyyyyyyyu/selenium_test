# -*- coding: UTF-8 -*-
# @Time     :2020/9/13 11:42
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import os
import time

import pytest
from selenium import webdriver
from PageObject.page_login import Login_Page
from Common.handle_excel import Handle_Excel
from Common.handle_path import DataPath
from Common.handle_config import conf


@pytest.fixture(scope="class")
def login_fixture():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = Login_Page(driver)
    yield login_page
    driver.quit()


class TestLoginCase:
    DataPath = os.path.join(DataPath, 'gs_testcase.xlsx')
    excel = Handle_Excel(DataPath, 'login')
    datas = excel.read_excel()

    @pytest.mark.parametrize('case', datas)
    def test_login_suc(self, case, login_fixture):
        login_page = login_fixture
        user = case['username']
        pwd = case['password']
        url = conf.get('Env', 'url')
        login_page.get_url(url)
        login_page.login(user, pwd)
        time.sleep(0.1)
        login_page.silde_runing()
        login_page.click_login()
        time.sleep(1.8)
        login_page.click_logout()


if __name__ == '__main__':
    pytest.main(['-sv', '-k', 'login'])
