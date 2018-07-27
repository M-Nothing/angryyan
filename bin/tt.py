# coding:utf-8
import logging
import traceback
import json
import md5
import os
from collections import Counter
from xmcommon.web import core
from xmcommon.base.response import error, success
from xmcommon.base.resptools import RESPRET

log = logging.getLogger()

class IndexHandler(core.Handler):
    def GET(self):
        data = []
        try:
            with open("/home/owner/tmp.json","r") as f:
                data = json.load(f)
                json_str = json.dumps(data)
        except:
            log.error(traceback.format_exc())
        return self.render('test.html')


class DataInitHandler(core.Handler):
    def GET(self):
        data = []
        try:
            with open("/home/owner/tmp.json","r") as f:
                json_str = json.load(f)
                data = json.loads(json_str)
        except:
            log.error(traceback.format_exc())
            return self.write(error(errcode=RESPRET.PARAMERR, respmsg="文件不存在或解析失败"))
        return self.write(success({'data': data, 'json_str': json_str}))


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
        return self.write(success({"data": json.loads(json_data)}))


class DataDealHandler(core.Handler):
    def POST(self):
        params = self.req.input()
        del_index = params.get("del_index", '')
        new_data = []
        try:
            del_index = int(del_index)
            with open("/home/owner/tmp.json","r") as f:
                old_data = json.loads(json.load(f))
                new_data = old_data[:del_index] + old_data[del_index+1:]
                f.close()
            with open("/home/owner/tmp.json","w") as f:
                json.dump(json.dumps(new_data), f)
            nd_str = json.dumps(new_data)
        except:
            log.error(traceback.format_exc())
            return self.write(error(errcode=RESPRET.PARAMERR, respmsg="系统错误"))

        return self.write(success({'data': new_data, 'json_str': nd_str}))


class SqlDealHandler(core.Handler):
    def POST(self):
        file_path = "/home/owner/logs/tmp.log"
        # 上传文件到服务器  并保存
        ret = []
        params = self.req.input()
        r_file = params.get('file', '')
        if not r_file:
            return self.write(RESPRET.UNKNOWERR, error(respmsg='上传文件失败'))
        r_data = r_file.read()
        op_file = open(file_path, 'w')
        op_file.write(r_data)
        op_file.close()
        log_data = os.popen('grep -E "DELETE|INSERT|UPDATE|SELECT" %s' % file_path).read().strip().split('\n')
        count_dict = {}
        for l in log_data:
            key = "%s_%s" % (l[0:16], l[21: -1])
            if l[0:16] and count_dict.has_key(l[0:16]):
                count_dict[l[0:16]].update({l[21: -1]: count_dict[l[0:16]].get(l[21: -1], 0)+1})
            else:
                count_dict.update({l[0: 16]: {l[21:-1]: 1}})
        ret = map(lambda x: {x: sorted(count_dict[x].iteritems(), key=lambda e: -e[1])}, count_dict.keys())
        ret_dict = {}
        for item in ret:
            for r_k, r_v in item.iteritems():
                print r_k, r_v
                v = 0
                for rv in range(0, len(r_v)):
                    print r_v[rv], r_v[rv][1], v
                    if r_v[rv] and r_v[rv][1] >= v:
                        v = r_v[rv][1]
                    else:
                        ret_dict.update({r_k: r_v[0: rv]})
                        rv = len(r_v)
                if not ret_dict.get(r_k):
                    ret_dict.update({r_k: r_v})
        return self.write(success({'data': ret_dict}))
