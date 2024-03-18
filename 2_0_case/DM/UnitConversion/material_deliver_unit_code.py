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

    print("访问月度发货")

    deliveries_response = \
        req.visit("post",
                  "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                  json={
                      'express': 'deliveries',
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
    deliveries_dict = deliveries_response['rows']
    print("返回元组", deliveries_dict)

    for item1 in materialDictionaries_dict:
        for item2 in deliveries_dict:
            if item1['materialId'] == item2['productId']:
                print("物料主数据产品代码", item1['materialId'], "月度发货产品代码", item2['productId'])

                mainUnitCode = [material['mainUnitCode'] for material in materialDictionaries_dict if
                                material['materialId'] == item2['productId']][0]

                print("物料主数据产品代码", item1['materialId'], "主计量单位", mainUnitCode)

                deliveries_unitCode = [deliverie['unitCode'] for deliverie in deliveries_dict if
                                       item1['materialId'] == deliverie['productId']][0]

                print("月度发货产品代码", item2['productId'], "月度发货主计量单位", deliveries_unitCode)

                hasUnitConvert = [deliverie['hasUnitConvert'] for deliverie in deliveries_dict if
                                  deliverie['productId'] == item1['materialId']][0]

                # print(hasUnitConvert)
                print("月度发货单位转换标记", hasUnitConvert)

                if mainUnitCode == deliveries_unitCode and hasUnitConvert == True:
                    print("测试通过")
                elif mainUnitCode != deliveries_unitCode and hasUnitConvert == False:
                    print("测试通过")
                else:
                    print("测试不通过")
