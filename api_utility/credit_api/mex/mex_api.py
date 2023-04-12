
# 接口的方法定义，后面的测试case直接调用，以免case代码看起来多大一坨
from url_gather.api_util import api_util

from tool.response_util import process_response


def mobile_query(params):
    response = api_util.get_mobile_belong(parmas=params)
    process_response(response)
    return response.json()


def post_json(parmas):
    """
    post接口
    :return:
    """
    response = api_util.post_mobile_belong(parmas=parmas)
    process_response(response)
    return response.json()

# -------------------------------------分割线--------------------------------------
# def queryAvailableProduct(params):
#     response = Api().get_regsiter_belong(params)
#     return response.json()
