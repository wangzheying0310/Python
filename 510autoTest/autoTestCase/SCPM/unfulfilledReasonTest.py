# -- coding:utf-8 --
import requests
import allure
from data.decorators import data


# 测试需求不满足原因不展示的情况
@allure.epic("Demand")
class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        """关闭session"""


if __name__ == '__main__':
    # 万能登录请求
    url = 'http://172.16.5.10/apim/v2/auth/login'
    payload = {
        "userNo": "WZY",
        "passWord": "MTIzNDU2",
        "verifierCode": ""
    }
    req = RequestHandler()

    headers = {
        'Content-Type': 'application/json',
        'GoUsrNo': 'WZY',
    }

    token = req.visit("post", url, json=payload, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    PISPIP_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model01/computeExprDatas",
                  json={
                      'ProductInStockingPointInPeriod': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 5000,
                          },
                      },
                  }, headers=headers).json()["data"]

    ProductInStockingPointInPeriod_dict = PISPIP_response['ProductInStockingPointInPeriod']

    unfulfilledReason_list = [row['unfulfilledReason'] for row in ProductInStockingPointInPeriod_dict['rows'] if
                              row['unfulfilledReason'] != '']

    print(unfulfilledReason_list)
    print("不满足原因个数", len(unfulfilledReason_list))

    allUnfulfilledDemandQuantityForOG_list = [row['allUnfulfilledDemandQuantityForOG'] for row in
                                              ProductInStockingPointInPeriod_dict['rows'] if
                                              row['allUnfulfilledDemandQuantityForOG'] != 0]

    print(allUnfulfilledDemandQuantityForOG_list)
    print("不满足量个数", len(allUnfulfilledDemandQuantityForOG_list))

    if len(unfulfilledReason_list) == len(allUnfulfilledDemandQuantityForOG_list):
        print("测试通过")
    else:
        print("存在有未满足量但无满足原因情况")