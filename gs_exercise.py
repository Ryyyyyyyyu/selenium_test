# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 12:37
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.gszwfw.gov.cn/'
driver.get(url)

driver.implicitly_wait(10)

time.sleep(0.5)
driver.switch_to.frame('sydlzc2019')
login = driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div").click()

username = driver.find_element(By.XPATH, "//input[@name='username']")
username.clear()
username.send_keys('data123')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.clear()
password.send_keys('wan0801HS ')

slider = driver.find_element(By.XPATH, "//*[@id='verify_bar']/div")
gap = driver.find_element(By.XPATH, "//*[@id='verify-code']/div/div/div[2]")
act = ActionChains(driver)
act.click_and_hold(slider).perform()
act.drag_and_drop(slider, gap).perform()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()
a = driver.find_element(By.XPATH, "//*[@id='layui-layer1']/div").text
time.sleep(0.3)
assert a == '登录成功'
time.sleep(5)
driver.quit()
