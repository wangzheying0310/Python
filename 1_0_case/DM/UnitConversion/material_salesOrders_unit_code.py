# -- coding:utf-8 --
import requests


# 基础信息全部填写为DB

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
    response = requests.post('http://172.16.5.10/apim/v2/auth/login', headers=headers, json=payload,
                             verify=False)
    print("访问状态码", response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print("token", token)

    print("访问物料主数据")

    materialDictionaries_response = \
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

    materialDictionaries_dict = materialDictionaries_response['MaterialDictionaryInDM']

    materialDictionaries_list = materialDictionaries_dict['rows']

    print("物料主数据集合", materialDictionaries_list)

    print("访问销售需求")

    SalesOrderInDM_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'SalesOrderInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    SalesOrderInDM_dict = SalesOrderInDM_response['SalesOrderInDM']

    SalesOrderInDM_list = SalesOrderInDM_dict['rows']

    print("销售需求集合", SalesOrderInDM_list)

    # 遍历billOfMaterials_dict
    for item1 in SalesOrderInDM_list:

        # 遍历materialDictionaries_dict
        for item2 in materialDictionaries_list:

            # 如果Item1的productId等于Item2的materialId
            if item1['productId'] == item2['materialNr']:

                # 打印Item1的productId和Item2的materialId
                print("销售需求产品代码与物料主数据物料代码相同的数据", item1['productId'], item2['materialNr'])

                # 在materialDictionaries_dict找到item2['materialId']的mainUnitCode
                main_unit_code_pro = [product['unitCode'] for product in SalesOrderInDM_list if
                                      product['productId'] == item2['materialNr']][0]

                print("销售需求产品代码", item1['productId'], "产品主计量单位", main_unit_code_pro)

                raw_material_unit_code_pro = [material['mainUnitCode'] for material in materialDictionaries_list if
                                              item1['productId'] == material['materialNr']][0]

                print("物料主数据产品代码", item2['materialNr'], "产品主计量单位", raw_material_unit_code_pro)

                lackProductUnitConvert = [product['lackUnitConvert'] for product in SalesOrderInDM_list if
                                          product['productId'] == item2['materialNr']][0]

                print("销售需求中的产品单位转换标记", lackProductUnitConvert)

                if main_unit_code_pro == raw_material_unit_code_pro and lackProductUnitConvert == False:
                    print("测试通过")
                elif main_unit_code_pro != raw_material_unit_code_pro and lackProductUnitConvert == True:
                    print("测试通过")
                else:
                    print("测试不通过")
