#-*-coding:utf-8-*-
import logging
import traceback
from xmcommon.web import core

class LoginHandler(core.Handler):
    def GET(self):
        return self.render('login.html')
