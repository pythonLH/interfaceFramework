import pytest
import requests
import json

# 所有用例的前置步骤都可以放到这里面，然后具体的case需要用到，就直接继承调用就是，更灵活
from tool.log import Log


@pytest.fixture(scope="session", autouse=False)
def test_session():
    print("这是session级的fixture,在所有test_.py文件运行前，执行一次")


@pytest.fixture(scope="function", autouse=False)
def function_fixture():
    print("我是前置方法")
    # yield可以放在fixture任何一个等级中
    yield "这是yield返回的数据,可以用但实际工作中,不常用"
    print("我是后置方法")


# 接口测试的function全都会自动调用这个fixture前后置
@pytest.fixture(scope="function", autouse=True)
def function_fixture_2():
    Log().info("-----------------------开始执行测试用例-----------------------\n")
    yield
    Log().info("-----------------------结束执行测试用例-----------------------")


# 夹具中放个登录的请求方法，把token拿到后  用于后面其他接口调用
@pytest.fixture(scope="class", autouse=False)
def class_fixture():
    url = "http://192.168.122.239:7037/hc/app/noAuth/logon/login"

    payload = json.dumps({
        "promotionChannels": "googlePlay",
        "password": "",
        "flag": 1,
        "phone": "3526598799",
        "shortNo": "9999"
    })
    headers = {
        'app-name': 'Hinance',
        'app-version': '1.0.7',
        'channel': 'googlePlay',
        'commercialId': '01',
        'lang': 'zh',
        'organizationId': 'DCMEX',
        'token': '',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload).json()
    # 接口依赖，下个接口调用，需要用到的东西
    print(response["data"]["token"])
    return response["data"]["token"]


@pytest.fixture(scope="module", autouse=False)
def module_fixture():
    print("\n测试数据前置,方法级")
