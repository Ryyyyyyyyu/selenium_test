# -*- coding: UTF-8 -*-
# @Time     :2020/9/15 23:02
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import cv2
import requests


class Handle_Picture:

    def find_picture(self, target, template):
        """
        识别两张图片的最佳匹配
        :param target: 背景图片
        :param template:缺口图片
        :return:最佳匹配的X坐标
        """
        # 读取图片
        target_rgb = cv2.imread(target)
        # 灰度处理
        target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
        # 读取模块图片
        template_rbg = cv2.imread(template, 0)
        # 匹配模块位置
        res = cv2.matchTemplate(target_gray, template_rbg, cv2.TM_CCOEFF_NORMED)
        # 获取最佳与最差匹配
        value = cv2.minMaxLoc(res)
        # 返回最佳匹配的X坐标
        p = 280 / 680
        x = value[2][0] * p - 22
        return x

    def download_pic(self, url, picture_path):
        response = requests.request('get', url)
        with open(file=picture_path, mode='wb') as f:
            f.write(response.content)
        return picture_path
