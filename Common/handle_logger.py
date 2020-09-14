# -*- coding: UTF-8 -*-
# @Time     :2020/9/14 12:10
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import logging
import os
import time
from Common.handle_config import conf
from Common.handle_path import LogPath

now = time.strftime('%Y-%m-%d-')
filename = now + conf.get('log', 'filename')
log_path = os.path.join(LogPath, filename)


class Handle_logging:

    def handle_logging(self):
        mylog = logging.getLogger('raoyu')
        mylog.setLevel(conf.get('log', 'level'))

        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log', 'sh_level'))

        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(conf.get('log', 'fh_level'))

        mylog.addHandler(sh)
        mylog.addHandler(fh)

        formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        myformats = logging.Formatter(formats)
        sh.setFormatter(myformats)
        fh.setFormatter(myformats)

        return mylog


log = Handle_logging().handle_logging()
