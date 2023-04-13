import json

import requests

from tool.log import Log
from tool.read import middleground_conf


class RRRrestClient(object):
    def __init__(self):
        # 这个域名是配置文件里面的，传信贷的就调信贷的，传中台就调中台的，回头整个开关
        self.conf_url = middleground_conf

    def get(self, url_, header, data):

        return self.requets_(method="GET", url_=url_, header_=header, data=data)

    def post(self, url_, header, data):
        return self.requets_(method="POST", url_=url_, header_=header, data=data)

    def put(self, url_, header, data):
        return self.requets_(method="PUT", url_=url_, header_=header, data=data)

    def delete(self, url_, header, data):
        return self.requets_(method="DELETE", url_=url_, header_=header, data=data)

    def requets_(self, method, url_, header_, data):
        self.logger_(method, url_, data)

        if method == "GET":
            return requests.request("GET", self.conf_url + url_, headers=header_, data=data)

        elif method == "POST":
            return requests.request("POST", self.conf_url + url_, headers=header_, data=data)

        elif method == "PUT":
            requests.request("PUT", self.conf_url + url_, headers=header_, data=data)

        elif method == "DELETE":
            requests.request("DELETE", self.conf_url + url_, headers=header_, data=data)

    @staticmethod
    def logger_(method, url_, parmas):
        Log().debug("接口请求的方式：{}".format(method))
        Log().debug("接口请求的地址: {}".format(url_))
        Log().debug("接口请求的参数: {}".format(json.dumps(parmas, indent=2)))


if __name__ == '__main__':
    url = "/tele-marketing-platform/v1/case/loan/history/list?mobile=639565118500"
    payload = json.dumps({
        "intoCaseBeginTime": "2023-03-14 00:00:00",
        "intoCaseEndTime": "2023-04-13 23:59:59",
        "page": 1,
        "pageSize": 10,
        "country": ""
    })
    header = {
        'Content-Type': 'application/json; charset=UTF-8',
        'lang': 'zh_CN',
        'Authorization': 'd236b727-b39a-4bd6-97c1-a9f2d7c21f69',
        'userId': '167'
    }

    r = RRRrestClient().get(url, header, {}).json()
    print(r)
    # resp = requests.post("http://192.168.122.183:9080/test/tele-marketing-platform/v1/loan/case/list"
    #                      , payload, header)
    # url = "http://192.168.122.183:9080/test/tele-marketing-platform/v1/loan/case/list"
    #
    # payload = json.dumps({
    #     "intoCaseBeginTime": "2023-03-14 00:00:00",
    #     "intoCaseEndTime": "2023-04-13 23:59:59",
    #     "page": 1,
    #     "pageSize": 10,
    #     "country": ""
    # })
    # headers = {
    #     'Content-Type': 'application/json',
    #     'lang': 'zh_CN',
    #     'Authorization': 'b7f792ee-571c-4e1c-b6e1-fa1ea59e9b8c',
    #     'userId': '167'
    # }
    #
    # response = requests.post("POST", url, data=payload, json=headers)
    #
    # print(response.text)
