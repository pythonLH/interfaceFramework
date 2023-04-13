import pytest

from tool.httpqequest import RRRrestClient


class middleground(RRRrestClient):

    def __init__(self):
        super(middleground, self).__init__()
        self.headr = {
            'Content-Type': 'application/json',
            'lang': 'zh_CN',
            'Authorization': 'b7f792ee-571c-4e1c-b6e1-fa1ea59e9b8c',
            'userId': '167'
        }

    # 入库管理列表
    def loan_case_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 案件库管理列表
    def case_allocated_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 拨打根据记录列表
    def case_talk_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 历史借贷合同
    def loan_history_list(self, parmas):
        return self.get(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 我的案件列表
    def case_allocated_list_(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 结案管理列表
    def loan_case_finish_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 电销人员管理列表
    def assignee_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 电销组管理列表
    def assignee_group_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 电销人员统计列表
    def assignee_statistics_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 入库策略列表
    def storage_strategy_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 字典表维护列表
    def dictionary_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 推荐产品配置列表
    def recommend_product_page(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/loan/case/list', header=self.headr, data=parmas)

    # 圈人配置列表
    def mark_people_list(self, parmas):
        return self.post(url_='/tele-marketing-platform/v1/mark/people/list', header=self.headr, data=parmas)


middleground_util = middleground()
