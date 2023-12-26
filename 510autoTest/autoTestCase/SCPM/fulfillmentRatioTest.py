# -- coding:utf-8 --

import requests

from data.decorators import data


# 测试需求满足率计算是否正确
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
    # print(response)
    ProductInStockingPointInPeriod_dict = PISPIP_response['ProductInStockingPointInPeriod']

    salesDemandQuantity_list = [row['salesDemandQuantity'] for row in ProductInStockingPointInPeriod_dict['rows'] if
                                row['salesDemandQuantity'] != 0]

    # print("获取PISPIP中的salesDemandQuantity值（去掉为0的值）", salesDemandQuantity_list)

    salesDemandQuantity_total = sum(salesDemandQuantity_list)

    print("对salesDemandQuantity进行求和", salesDemandQuantity_total)

    print("对salesDemandQuantity进行求和（取整）", round(salesDemandQuantity_total))

    fulfilledDemandQuantity_list = [row['fulfilledDemandQuantity'] for row in
                                    ProductInStockingPointInPeriod_dict['rows'] if
                                    row['fulfilledDemandQuantity'] != 0]

    # print("获取PISPIP中的fulfilledDemandQuantity值（去掉为0的值）", fulfilledDemandQuantity_list)

    fulfilledDemandQuantity_total = sum(fulfilledDemandQuantity_list)

    print("对fulfilledDemandQuantity进行求和", fulfilledDemandQuantity_total)

    print("对fulfilledDemandQuantity进行求和（取整）", round(fulfilledDemandQuantity_total))

    dependentDemandQuantity_list = [row['dependentDemandQuantity'] for row in
                                    ProductInStockingPointInPeriod_dict['rows'] if
                                    row['dependentDemandQuantity'] != 0]

    # print("获取PISPIP中的dependentDemandQuantity值（去掉为0的值）", dependentDemandQuantity_list)

    dependentDemandQuantity_total = sum(dependentDemandQuantity_list)

    print("对dependentDemandQuantity进行求和", dependentDemandQuantity_total)

    print("对dependentDemandQuantity进行求和（取整）", round(dependentDemandQuantity_total))

    fulfilledDemandQuantity = fulfilledDemandQuantity_total - dependentDemandQuantity_total

    print("满足量为", fulfilledDemandQuantity)

    fulfillmentRatio = round(
        ((fulfilledDemandQuantity_total - dependentDemandQuantity_total) / salesDemandQuantity_total) * 100, 2)

    print("需求满足率为：", fulfillmentRatio, "%")

    BusinessKPI_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model01/computeExprDatas",
                  json={
                      'BusinessKPI': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    # print(BusinessKPI_response)

    BusinessKPI_dict = BusinessKPI_response['BusinessKPI']

    BusinessKPI_list = [row['fulfillmentRatio'] for row in BusinessKPI_dict['rows']]

    print("获取BusinessKPI中的fulfillmentRatio值", BusinessKPI_list[0])

    if BusinessKPI_list[0] == fulfillmentRatio:
        print("值相等，测试通过")
    else:
        print("值不相等，测试未通过")
