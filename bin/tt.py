# coding:utf-8
import logging
import traceback
import json
import os
from collections import Counter
from xmcommon.web import core
from xmcommon.base.response import error, success
from xmcommon.base.resptools import RESPRET

class IndexHandler(core.Handler):
    def GET(self):
        data = []
        try:
            with open("/home/owner/tmp.json","r") as f:
                data = json.load(f)
                json_str = json.dumps(data)
        except:
            log.error(traceback.format_exc())
        return self.render('test.html', data, json_str)


class DataUploadHandler(core.Handler):
    def POST(self):
        params = self.req.input()
        json_data = params.get('json_data', [])
        try:
            json.loads(json_data)
            with open("/home/owner/tmp.json","w") as f:
                json.dump(json_data, f)
        except:
            log.error(traceback.format_exc())
            return self.write(error(errcode=RESPRET.PARAMERR, respmsg="指定格式参数解析失败"))
        return self.write(success({}))


class DataDealHandler(core.Handler):
    def POST(self):
        params = self.req.input()
        del_index = params.get("del_index", '')
        new_data = []
        try:
            del_index = int(del_index)
            with open("/home/owner/tmp.json","wr") as f:
                old_data = json.load(f)
                new_data = old_data[0:del_index] + old_data[del_index+1:-1]
                json.dump(new_data, f)
        nd_str = json.dumps(new_data)
        return self.render("tt_test.html", new_data, nd_str)


class SqlDealHandler(core.Handler):
    def POST(self):
        file_path = "/Home/owner/logs/tmp.log"
        # 上传文件到服务器  并保存
        r_file = params.get('file', '')
        if not r_file:
            return self.write(RESPRET.UNKNOWERR, error(respmsg='上传文件失败'))
        r_data = r_file.read()
        op_file = open(file_path, 'w')
        op_file.write(r_data)
        op_file.close()
        log_data = os.popen('grep -E "DELETE|INSERT|UPDATE|SELECT" %s' % file_path).read().split('\n')
        c = Counter()
        for l in log_data:
            c.update({l[0:16]: 1})
        return self.write(success(dict(c)))
