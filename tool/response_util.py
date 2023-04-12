import json
from tool.log import Log


def process_response(response):
    ResultResponse = {}
    if response.status_code == 200:
        ResultResponse['success'] = True
        ResultResponse['body'] = response.json()
    else:
        ResultResponse['success'] = False
        Log().info("接口状态码不是2开头，请检查")
    Log().debug("接口响应结果是:{}".format(json.dumps(response.json(), indent=2)))
    return ResultResponse
