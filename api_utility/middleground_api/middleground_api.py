from url_gather.middleground_url import middleground_util
from tool.response_util import process_response


def loan_case_list(params):
    """
    # 入库管理列表
    :param params:
    :return:
    """
    response = middleground_util.loan_case_list(parmas=params)
    process_response(response)
    return response.json()


def case_allocated_list(parmas):
    """
    # 案件库管理列表
    :return:
    """
    response = middleground_util.case_allocated_list(parmas=parmas)
    process_response(response)
    return response.json()


def case_talk_list(parmas):
    """
    # 拨打根据记录列表
    :return:
    """
    response = middleground_util.case_talk_list(parmas=parmas)
    process_response(response)
    return response.json()


def loan_history_list(parmas):
    """
    # 历史借贷合同
    :return:
    """
    response = middleground_util.loan_history_list(parmas=parmas)
    process_response(response)
    return response.json()


def case_allocated_list_(parmas):
    """
    # 我的案件列表
    :return:
    """
    response = middleground_util.case_allocated_list_(parmas=parmas)
    process_response(response)
    return response.json()


def loan_case_finish_list(parmas):
    """
    # 结案管理列表
    :return:
    """
    response = middleground_util.loan_case_finish_list(parmas=parmas)
    process_response(response)
    return response.json()


def assignee_list(parmas):
    """
    # 电销人员管理列表
    :return:
    """
    response = middleground_util.assignee_list(parmas=parmas)
    process_response(response)
    return response.json()


def assignee_group_list(parmas):
    """
    # 电销组管理列表
    :return:
    """
    response = middleground_util.assignee_group_list(parmas=parmas)
    process_response(response)
    return response.json()


def assignee_statistics_list(parmas):
    """
    # 电销人员统计列表
    :return:
    """
    response = middleground_util.assignee_statistics_list(parmas=parmas)
    process_response(response)
    return response.json()


def storage_strategy_list(parmas):
    """
    # 入库策略列表
    :return:
    """
    response = middleground_util.storage_strategy_list(parmas=parmas)
    process_response(response)
    return response.json()


def dictionary_list(parmas):
    """
    # 字典表维护列表
    :return:
    """
    response = middleground_util.dictionary_list(parmas=parmas)
    process_response(response)
    return response.json()


def recommend_product_page(parmas):
    """
    # 推荐产品配置列表
    :return:
    """
    response = middleground_util.recommend_product_page(parmas=parmas)
    process_response(response)
    return response.json()


def mark_people_list(parmas):
    """
    # 圈人配置列表
    :return:
    """
    response = middleground_util.mark_people_list(parmas=parmas)
    process_response(response)
    return response.json()
