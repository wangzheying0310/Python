# -- coding:utf-8 --
import requests
from datetime import datetime, timedelta


class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        """关闭session"""

# DM采购订单数量与SCPM采购订单数量对比

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
    response = requests.post('http://172.16.5.10/apim/v2/auth/login', headers=headers, json=payload,
                             verify=False)
    print("访问状态码", response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print("token", token)

    PurchaseOrder_response = req.visit("post",
                                       "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/computeExprDatas",
                                       json={
                                           'PurchaseOrder': {
                                               'condition': '',
                                               'sort': '',
                                               'computeExprs': {},
                                               '__page': {
                                                   'num': 1,
                                                   'size': 300,
                                               },
                                           },
                                       }, headers=headers).json()["data"]

    PurchaseOrder_dict = PurchaseOrder_response['PurchaseOrder']

    PurchaseOrder_list = PurchaseOrder_dict['rows']

    print('供应链采购订单个数', PurchaseOrder_dict['total'])

    # print("供应链采购订单集合", PurchaseOrder_list)
    # 获取采购订单的系统时间

    scpTime = [item['scpTime'] for item in PurchaseOrder_list][0]
    print('系统时间', scpTime)
    # 获取DM采购订单
    PurchaseOrderInDM_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'PurchaseOrderInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {
                          },
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    PurchaseOrderInDM_dict = PurchaseOrderInDM_response['PurchaseOrderInDM']

    PurchaseOrderInDM_list = PurchaseOrderInDM_dict['rows']

    # print("Dm采购订单集合", PurchaseOrderInDM_list)

    print('DM采购订单个数', PurchaseOrderInDM_dict['total'])

    if PurchaseOrder_dict['total'] == PurchaseOrderInDM_dict['total']:
        print("个数一致，测试通过")
    else:
        print("测试未通过")

    print('采购临近到货判断')
    for item in PurchaseOrder_list:
        backlog_days = int(item['nearInboundRemindDays'].split(' ')[0])

        item['nearInboundRemindDays'] = str(backlog_days).zfill(2)

    for item in PurchaseOrder_list:

        inbound_date = datetime.strptime(item['planToDeliverDate'], '%Y-%m-%d')

        compare_date = datetime.strptime(scpTime, '%Y-%m-%d %H:%M:%S')

        if inbound_date - timedelta(days=int(item['nearInboundRemindDays'])) < compare_date and item['nearInboundWarning'] == True:

            print(f"{item['materialId']}已到货，预计到货预警为{item['nearInboundWarning']},预计到货-采购临近到货预警时间为{inbound_date - timedelta(days=int(item['nearInboundRemindDays']))}，到货时间为{inbound_date}，天数为{timedelta(days=int(item['nearInboundRemindDays']))}，测试通过")

        elif inbound_date - timedelta(days=int(item['nearInboundRemindDays'])) > compare_date and item['nearInboundWarning'] == False:

            print(f"{item['materialId']}未到货，预计到货预警为{item['nearInboundWarning']}，预计到货-采购临近到货预警时间为{inbound_date - timedelta(days=int(item['nearInboundRemindDays']))}，到货时间为{inbound_date}，天数为{timedelta(days=int(item['nearInboundRemindDays']))}，测试通过")
        else:
            print('测试不通过')

