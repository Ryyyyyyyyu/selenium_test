# -*- coding: UTF-8 -*-
# @Time     :2020/9/12 14:16
# @Author   :raoyu
# @Email    :2458757210@qq.com
# @Phone    :18893703014
import os

# 项目目录路径
ProjectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
ConfigPath = os.path.join(ProjectPath, 'Config')

# 页面基础操作路径
BasePath = os.path.join(ProjectPath, 'Base')

# 日志文件路径
LogPath = os.path.join(ProjectPath, 'Logs')

# 测试数据文件路径
DataPath = os.path.join(ProjectPath, 'Data')

# 页面操作逻辑代码文件路径
PagePath = os.path.join(ProjectPath, 'PageObject')

# 测试报告路径
ReportPath = os.path.join(ProjectPath, 'Reports')

# 测试用例代码路径
CasePath = os.path.join(ProjectPath, 'TestCase')
