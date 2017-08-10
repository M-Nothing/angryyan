# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import os
import sys
from webconfig import *

# 服务地址
HOST = '0.0.0.0'

# 服务端口
PORT = 9099

# 调试模式: True/False
# 生产环境必须为False
DEBUG = False
PRO_NAME = 'angryyan'

# 日志文件配置
if DEBUG:
    LOGFILE = 'stdout'
else :
    LOGFILE = {
        'root': {
            'filename': {
                'DEBUG': os.path.join(HOME,'../log','{}.info.log'.format(PRO_NAME)),
                'ERROR': os.path.join(HOME,'../log','{}.error.log'.format(PRO_NAME)),
            },
        }
    }

# 数据库配置
DATABASE = {
    'angryyan': {
        'engine':'mysql',
        'db': 'angryyan',
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'abc.123',
        'charset': 'utf8',
        'conn': 16,
    },
}

