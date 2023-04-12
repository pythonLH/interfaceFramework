import pytest
from api_utility.credit_api.mex.mex_api import post_json
from tool.read import red_data


def test_post():
    json_data = red_data["json_data"]
    result = post_json(json_data)

    # 断言
    assert result['status'] == '101'
    assert result['msg'] == "APPKEY不存在"


if __name__ == '__main__':
    pytest.main()
