import json

import pytest
from tool.read import red_data
# 引入所有case对应的api
from api_utility.middleground_api.middleground_api import loan_case_list, \
    case_allocated_list, \
    case_talk_list, \
    loan_history_list, \
    case_allocated_list_, \
    loan_case_finish_list, \
    assignee_list, \
    assignee_group_list, \
    assignee_statistics_list, \
    storage_strategy_list, \
    dictionary_list, \
    recommend_product_page, \
    mark_people_list


# case里面就直接调用api封装的请求方法，达到一个requests请求,跟testcase分离的效果
def test_loan_case_list():
    result = loan_case_list(json.dumps(red_data["loan_case_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_case_allocated_list():
    result = case_allocated_list(json.dumps(red_data["case_allocated_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_case_talk_list():
    result = case_talk_list(json.dumps(red_data["case_talk_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_loan_history_list():
    result = loan_history_list(json.dumps(red_data["loan_history_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test__case_allocated_list():
    result = case_allocated_list_(json.dumps(red_data["_case_allocated_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_loan_case_finish_list():
    result = loan_case_finish_list(json.dumps(red_data["loan_case_finish_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_assignee_list():
    result = assignee_list(json.dumps(red_data["assignee_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_assignee_group_list():
    result = assignee_group_list(json.dumps(red_data["assignee_group_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_assignee_statistics_list():
    result = assignee_statistics_list(json.dumps(red_data["assignee_statistics_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_storage_strategy_list():
    result = storage_strategy_list(json.dumps(red_data["storage_strategy_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_dictionary_list():
    result = dictionary_list(json.dumps(red_data["dictionary_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_recommend_product_page():
    result = recommend_product_page(json.dumps(red_data["recommend_product_page"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


def test_mark_people_list():
    result = mark_people_list(json.dumps(red_data["mark_people_list"]))
    # 断言
    assert result['code'] == 200
    assert result['msg'] == "success"
    assert result['success'] is True


# if __name__ == '__main__':
#     pytest.main()
