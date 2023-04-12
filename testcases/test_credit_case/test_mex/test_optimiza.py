import pytest

from api_utility.credit_api.mex.mex_api import mobile_query
from tool.read import red_data


# case里面就直接调用api封装的请求方法，达到一个requests请求,跟testcase分离的效果
def test_mobile():
    result = mobile_query(red_data["mobile_belong"])
    # 断言
    assert result['status'] == 0
    assert result['msg'] == "ok"


if __name__ == '__main__':
    pytest.main()
