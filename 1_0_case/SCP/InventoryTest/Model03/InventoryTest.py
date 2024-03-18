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

# 物料积压预警

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

    Inventory_response = req.visit("post",
                                   "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/computeExprDatas",
                                   json={
                                       'CurrentInventory': {
                                           'condition': '',
                                           'sort': '',
                                           'computeExprs': {},
                                           '__page': {
                                               'num': 1,
                                               'size': 300,
                                           },
                                       },
                                   }, headers=headers).json()["data"]

    Inventory_dict = Inventory_response['CurrentInventory']

    Inventory_list = Inventory_dict['rows']

    print('供应链库存个数', Inventory_dict['total'])

    print("供应链库存集合", Inventory_list)

    inventorySource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'InventoryInDM': {
                          'condition': '',
                          'sort': 'lackUnitConvert sort "asc"',
                          'computeExprs': {
                          },
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    inventorySource_dict = inventorySource_response['InventoryInDM']

    inventorySource_list = inventorySource_dict['rows']

    # print("库存集合", inventorySource_list)

    print('DM库存个数', inventorySource_dict['total'])

    if Inventory_dict['total'] == inventorySource_dict['total']:
        print("个数一致，测试通过")
    else:
        print("测试未通过")

    # 获取预警天数

    days = [item1['backlogRemindDays'] for item1 in Inventory_list if 'backlogRemindDays' in item1][0]

    # print('预警天数', days)

    PeriodDefinitionSequence_response = req.visit("post",
                                                  "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/computeExprDatas",
                                                  json={
                                                      'PeriodDefinitionSequence': {
                                                          'condition': '',
                                                          'sort': '',
                                                          'computeExprs': {},
                                                          '__page': {
                                                              'num': 1,
                                                              'size': 300,
                                                          },
                                                      },
                                                  }, headers=headers).json()["data"]

    PeriodDefinitionSequence_dict = PeriodDefinitionSequence_response['PeriodDefinitionSequence']

    PeriodDefinitionSequence_list = PeriodDefinitionSequence_dict['rows']

    # print('计划周期集合', PeriodDefinitionSequence_list)

    startData = [item['start'] for item in PeriodDefinitionSequence_list][0]

    print('计划周期开始时间', startData)

    # 遍历集合，获取每个materialId的backlogRemindDays值并取前两位
    for item in Inventory_list:
        backlog_days = int(item['backlogRemindDays'].split(' ')[0])
        # print(backlog_days)
        item['backlogRemindDays'] = str(backlog_days).zfill(2)

    print('积压天数测试')
    # 比较每个materialId的inboundDate+backlogRemindDays值并取前两位是否大于2023-06-01 00:00:00
    for item in Inventory_list:

        inbound_date = datetime.strptime(item['inboundDate'], '%Y-%m-%d')

        # print('入库时间', inbound_date)

        compare_date = datetime.strptime(startData, '%Y-%m-%d %H:%M:%S')

        # print(compare_date)

        if inbound_date + timedelta(days=int(item['backlogRemindDays'])) > compare_date and item['backlogWarnings'] == False:

            print(f"{item['materialId']}未积压，积压预警为{item['backlogWarnings']},入库时间+积压天数时间为{inbound_date + timedelta(days=int(item['backlogRemindDays']))},测试通过")

        elif inbound_date + timedelta(days=int(item['backlogRemindDays'])) < compare_date and item['backlogWarnings'] == True:

            print(f"{item['materialId']}已积压,积压预警为{item['backlogWarnings']},入库时间+积压天数时间为{inbound_date + timedelta(days=int(item['backlogRemindDays']))}，测试通过")
        else:
            print('测试不通过')

    print('库存有效期判断')

    for item in Inventory_list:
        backlog_days = int(item['expireRemindDays'].split(' ')[0])
        item['expireRemindDays'] = str(backlog_days).zfill(2)

    for item in Inventory_list:

        inbound_date = datetime.strptime(item['expireDate'], '%Y-%m-%d')

        print('失效时间', inbound_date)

        compare_date = datetime.strptime(startData, '%Y-%m-%d %H:%M:%S')

        print('周期开始时间', compare_date)

        if inbound_date - timedelta(days=int(item['expireRemindDays'])) > compare_date and item['expireWarning'] == False:

            print(f"{item['materialId']}未失效,有效期-失效提醒天数时间为{inbound_date - timedelta(days=int(item['expireRemindDays']))},测试通过")

        elif inbound_date - timedelta(days=int(item['expireRemindDays'])) < compare_date and item['expireWarning'] == True:

            print(f"{item['materialId']}已失效，有效期-失效提醒天数时间为{inbound_date - timedelta(days=int(item['expireRemindDays']))}，测试通过")
        else:
            print('测试不通过')