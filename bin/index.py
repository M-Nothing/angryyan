#-*-coding:utf-8-*-
import logging
import traceback
from xmcommon.web import core

class IndexHandler(core.Handler):
    def GET(self):
        return self.redirect('/login')
