# -- coding:utf-8 --
import requests
from data.decorators import data

# 基础信息全部填写为WebService


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

    KT_BasicData_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0:Model03:1/add-kts",
                  json={
                      'createUser': 'WZY',
                      'branchName': '模式3',
                      'remark': '修改为WebService',
                      'vos': [
                          {
                              'ktIdentity': 'com.aps.model.dm.KTBasicDataSource',
                              'deleteAll': False,
                              'deleteIds': [],
                              'addRows': [],
                              'updateRows': [
                                  {
                                      'ktid': 0,
                                      'bomSource': 'WebService',
                                      'materialDicSource': 'WebService',
                                      'productionVersionSource': 'WebService',
                                      'supplierInfoSource': 'WebService',
                                      'unitConversionSource': 'WebService',
                                  },
                              ],
                          },
                      ],
                  }, headers=headers).json()["data"]
    synchronizeBasicDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeBasicDataForClient',
                      'args': [],
                      'userNo': 'WZY',
                  }, headers=headers).json()["data"]

    BOM_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'HandledBillOfMaterialInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    BOM_dict = BOM_response['HandledBillOfMaterialInDM']

    print(BOM_dict['total'])

    MaterialDictionary_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'MaterialDictionaryInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    MaterialDictionary_dict = MaterialDictionary_response['MaterialDictionaryInDM']

    print(MaterialDictionary_dict['total'])

    ProductionVersion_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'ProductionVersionInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    ProductionVersion_dict = ProductionVersion_response['ProductionVersionInDM']

    print(ProductionVersion_dict['total'])

    if BOM_dict['total'] == MaterialDictionary_dict['total'] == ProductionVersion_dict['total'] == 0:
        print("未获取到数据，测试通过")
    else:
        print("测试未通过")
