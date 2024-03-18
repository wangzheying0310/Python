# -- coding:utf-8 --
import requests


# 单位转换判断


class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        """关闭session"""


if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    url = 'http://172.16.9.2:42010/api/auth/authentication/login'
    payload = {
        "userNo": "wzy",
        "password": "RSO@2019"
    }
    req = RequestHandler()

    headers = {
        # 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJOTyI6Ind6eSIsImlzcyI6IkdPT0RPIiwiSUQiOiIxMDEiLCJleHAiOjE3MDAxOTQzNTMsImlhdCI6MTcwMDAxNDM1MywianRpIjoiVVNFUl9UT0tFTi4xMDEifQ.YUYb7YCvtKdLmohXEV2xXe58gYgy19HpBOi-N0TSP40',
        'Client-Identity': '8ff1592731cb56dc10926a2b2229999c',
        # 'Content-Type': 'application/json',
    }
    response = requests.post('http://172.16.9.2:42010/api/auth/authentication/login', headers=headers, json=payload,
                             verify=False)
    print("访问状态码", response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print("token", token)

    print("访问物料主数据")

    materialDictionaries_response = \
        req.visit("post",
                  "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                  json={
                      'express': 'this.materialDictionaries',
                      'page': {
                          'num': 1,
                          'size': 300,
                      },
                      'sort': [
                          {
                              'field': 'materialId',
                              'asc': True,
                              'order': 0,
                          },
                      ],
                      'expression': [],
                      'condition': '',
                      'statistics': {
                          'needRow': False,
                          'baseStatistics': {},
                      },
                  }, headers=headers).json()["data"]

    # print("返回请求值", materialDictionaries_response)
    materialDictionaries_dict = materialDictionaries_response['rows']
    print("返回元组", materialDictionaries_dict)

    print("访问采购申请")

    purchaseRequests_response = \
        req.visit("post",
                  "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                  json={
                      'express': 'purchaseRequests',
                      'page': {
                          'num': 1,
                          'size': 300,
                      },
                      'sort': [],
                      'expression': [],
                      'condition': '',
                      'statistics': {
                          'needRow': False,
                          'baseStatistics': {},
                      },
                  }, headers=headers).json()["data"]
    # print("返回请求值", deliveries_response)
    purchaseRequests_dict = purchaseRequests_response['rows']
    print("返回元组", purchaseRequests_dict)

    for item1 in materialDictionaries_dict:
        for item2 in purchaseRequests_dict:
            if item1['materialId'] == item2['productId']:
                print("物料主数据产品代码", item1['materialId'], "采购申请产品代码", item2['productId'])

                mainUnitCode = [material['mainUnitCode'] for material in materialDictionaries_dict if
                                material['materialId'] == item2['productId']][0]

                print("物料主数据产品代码", item1['materialId'], "主计量单位", mainUnitCode)

                Requests_unitCode = [Requests['unitCode'] for Requests in purchaseRequests_dict if
                                       item1['materialId'] == Requests['productId']][0]

                print("采购申请产品代码", item2['productId'], "采购申请主计量单位", Requests_unitCode)

                hasUnitConvert = [Requests['hasUnitConvert'] for Requests in purchaseRequests_dict if
                                  Requests['productId'] == item1['materialId']][0]

                # print(hasUnitConvert)
                print("采购申请单位转换标记", hasUnitConvert)

                if mainUnitCode == Requests_unitCode and hasUnitConvert == True:
                    print("测试通过")
                elif mainUnitCode != Requests_unitCode and hasUnitConvert == False:
                    print("测试通过")
                else:
                    print("测试不通过")
