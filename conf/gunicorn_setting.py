#!/usr/bin/env python
# encoding: utf-8
# 访问 http://tool.lu/pyc/ 查看更多信息
import os
import sys
HOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(HOME), 'conf'))
import config as myconfig
bind = '%s:%s' % (myconfig.HOST, myconfig.PORT)
chdir = os.path.join(os.path.dirname(HOME), 'bin')
workers = 4
threads = 16
worker_class = 'gevent'
backlog = 1024
timeout = 30
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s "%(f)s" "%(a)s"'
accesslog = os.path.join(HOME, '../log/gunicorn_access.log')
errorlog = os.path.join(HOME, '../log/gunicorn_error.log')
