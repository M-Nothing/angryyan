# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import os
import sys
import logging
from common.web import core
from common.base import dbpool
from common.base.dbpool import with_database

log = logging.getLogger()

class UploadFile(core.Handler):
    def GET(self):
        s = '''
        <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="haha" value="">
        <input type="submit" value="submit">
        </form>'''
        self.write(s)

    def POST(self):
        files = self.req.files()
        data = ''
        for f in files:
            data += f.value
            log.debug('name=%s filename=%s filelen=%s', f.name, f.filename, len(f.value))
        self.write(data)

