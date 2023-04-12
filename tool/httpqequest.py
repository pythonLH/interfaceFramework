import requests
import json

from tool.log import Log
from tool.read import test_host, yufa_host


class RRRrestClient(object):
    def __init__(self):
        self.api_root_url = test_host
        self.post_root_url = yufa_host

    def get(self, url_, parmas, **kwargs):

        return self.requets_(method="GET", url_=url_, parmas=parmas, **kwargs)

    def post(self, url_, parmas, **kwargs):
        return self.requets_(method="POST", url_=url_, parmas=parmas, **kwargs)

    def put(self, url_, parmas, **kwargs):
        return self.requets_("PUT", url_=url_, parmas=parmas, **kwargs)

    def delete(self, url_, parmas, **kwargs):
        return self.requets_("PUT", url_=url_, parmas=parmas, **kwargs)

    def requets_(self, method, url_, parmas, **kwargs):
        # 日志输出
        self.logger_(method, url_, parmas)

        if method == "GET":
            return requests.get(self.api_root_url + url_, parmas, **kwargs)

        elif method == "POST":
            return requests.post(self.post_root_url + url_, parmas, **kwargs)

        elif method == "PUT":
            requests.put(self.post_root_url + url_, data=None, **kwargs)

        elif method == "DELETE":
            requests.delete(self.post_root_url + url_, **kwargs)

    @staticmethod
    def logger_(method, url_, parmas):
        Log().debug("接口请求的方式：{}".format(method))
        Log().debug("接口请求的地址: {}".format(url_))
        Log().debug("接口请求的参数: {}".format(json.dumps(parmas, indent=2)))
