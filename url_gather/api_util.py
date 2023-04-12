# 需要测试的接口地址，单独放一个.py便于管理，因为可能有很多的接口需要测试
from tool.httpqequest import RRRrestClient


class AAPI(RRRrestClient):
    def __init__(self):
        super(AAPI, self).__init__()

    # **kwargs 字典形式传参数
    def get_mobile_belong(self, parmas, **kwargs):
        return self.get(url_='/shouji/query', parmas=parmas, **kwargs)

    def post_mobile_belong(self, parmas, **kwargs):
        return self.post(url_='/posts', parmas=parmas, **kwargs)


api_util = AAPI()

# -------------------------------------分割线--------------------------------------

# config_header = IniRead(ini_path).red_get('hc_header', 'api_header')

# class Api(RestClient):
#     def __init__(self):
#         # 父类需要传个接口地址
#         super(Api, self).__init__()
#
#     # 查询最大可借天数
#     def get_regsiter_belong(self, params):
#         return self.post("/hc/app/loan/queryAvailableProduct", eval(config_header), params)
