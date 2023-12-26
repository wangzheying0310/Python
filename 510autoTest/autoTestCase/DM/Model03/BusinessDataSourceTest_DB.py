# -- coding:utf-8 --
import requests
from data.decorators import data

# 业务信息全部填写为DB

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

    KT_BusinessData_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0:Model03:15/add-kts",
                  json={
                      'createUser': 'WZY',
                      'branchName': '模式3',
                      'remark': '修改为DB',
                      'vos': [
                          {
                              'ktIdentity': 'com.aps.model.dm.KTBusinessDataSource',
                              'deleteAll': False,
                              'deleteIds': [],
                              'addRows': [],
                              'updateRows': [
                                  {
                                      'ktid': 0,
                                      'deliverySource': 'DB',
                                      'inventorySource': 'DB',
                                      'purchaseOrderSource': 'DB',
                                      'purchaseRequestSource': 'DB',
                                  },
                              ],
                          },
                      ],
                  }, headers=headers).json()["data"]

    print(KT_BusinessData_response)

    synchronizeBusinessDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeBusinessDataForClient',
                      'args': [],
                      'userNo': 'WZY',
                  }, headers=headers).json()["data"]

    deliverySource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'MonthlyDeliveryInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    deliverySource_dict = deliverySource_response['MonthlyDeliveryInDM']

    print(deliverySource_dict['total'])

    inventorySource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'InventoryInDM': {
                          'condition': '',
                          'sort': 'lackUnitConvert sort "asc"',
                          'computeExprs': {
                              '缺少单位转换': {
                                  'type': 'icon',
                                  'field': '缺少单位转换',
                                  'describe': '缺少单位转换',
                                  'exp': [
                                      {
                                          'desc': '正常',
                                          'exp': 'var value = false; // 初始化value值\nif (object.lackUnitConvert === false) { // object是该表格中的列属性, somedata表示该列下的行数据\n    value = true; // 满足条件时value 为 true 将渲染出结果\n}',
                                          'icon': 'tick4',
                                          'origin': '',
                                      },
                                      {
                                          'desc': '单位转换是否正常',
                                          'exp': 'var value = false; // 初始化value值\nif (object.lackUnitConvert === true) { // object是该表格中的列属性, somedata表示该列下的行数据\n    value = true; // 满足条件时value 为 true 将渲染出结果\n}',
                                          'icon': 'forbidden1',
                                          'origin': '',
                                      },
                                  ],
                              },
                          },
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    inventorySource_dict = inventorySource_response['InventoryInDM']

    print(inventorySource_dict['total'])

    purchaseOrderSource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'PurchaseOrderInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    purchaseOrderSource_dict = purchaseOrderSource_response['PurchaseOrderInDM']

    print(purchaseOrderSource_dict['total'])

    purchaseRequestSource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'PurchaseRequestInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    purchaseRequestSource_dict = purchaseRequestSource_response['PurchaseRequestInDM']

    print(purchaseRequestSource_dict['total'])

    if deliverySource_dict['total'] == inventorySource_dict['total'] == purchaseOrderSource_dict['total'] == \
            purchaseRequestSource_dict['total'] == 0:
        print("未获取到数据，测试通过")
    else:
        print("测试未通过")
