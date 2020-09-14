# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 17:54
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import os
from configparser import ConfigParser
from Common.handle_path import ConfigPath


class Handle_config(ConfigParser):

    def __init__(self, filename):
        super().__init__(self)
        self.read(filenames=filename, encoding='utf-8')


ConfigPath = os.path.join(ConfigPath, 'config.ini')
conf = Handle_config(ConfigPath)
