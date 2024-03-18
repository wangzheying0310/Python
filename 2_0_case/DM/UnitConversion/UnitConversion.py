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

    materialDictionaries_dict = materialDictionaries_response['rows']

    print("访问BOM")

    billOfMaterials_response = \
        req.visit("post",
                  "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                  json={
                      'express': 'this.billOfMaterials',
                      'page': {
                          'num': 1,
                          'size': 300,
                      },
                      'sort': [
                          {
                              'field': 'productId',
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
    # print("返回请求值", billOfMaterials_response)
    billOfMaterials_dict = billOfMaterials_response['rows']
    # print("返回元组", billOfMaterials_dict)

    # 遍历billOfMaterials_dict
    for item1 in billOfMaterials_dict:

        # 遍历materialDictionaries_dict
        for item2 in materialDictionaries_dict:

            # 如果Item1的productId等于Item2的materialId
            if item1['productId'] == item2['materialId']:

                # 打印Item1的productId和Item2的materialId
                print("BOM产品代码与物料主数据物料代码相同的数据", item1['productId'], item2['materialId'])

                # 在materialDictionaries_dict找到item2['materialId']的mainUnitCode
                main_unit_code_pro = [product['productUnitCode'] for product in billOfMaterials_dict if
                                      product['productId'] == item2['materialId']][0]

                print("BOM产品代码", item1['productId'], "产品主计量单位", main_unit_code_pro)

                raw_material_unit_code_pro = [material['mainUnitCode'] for material in materialDictionaries_dict if
                                              item1['productId'] == material['materialId']][0]

                print("物料主数据产品代码", item2['materialId'], "产品主计量单位", raw_material_unit_code_pro)

                hasProductUnitConvert = [product['hasProductUnitConvert'] for product in billOfMaterials_dict if
                                         product['productId'] == item2['materialId']][0]

                print("BOM中的产品单位转换标记", hasProductUnitConvert)

                if main_unit_code_pro == raw_material_unit_code_pro and hasProductUnitConvert == True:
                    # print("产品单位不需要转换", True)
                    print("测试通过")
                elif main_unit_code_pro != raw_material_unit_code_pro and hasProductUnitConvert == False:
                    print("测试通过")
                else:
                    print("测试不通过")
                    # print("产品单位需要转换", False)

            #     如果item1['rawMaterialId'] == item2['materialId']
            elif item1['rawMaterialId'] == item2['materialId']:

                # 打印item1['rawMaterialId'], item2['materialId']
                print("BOM物料代码与物料主数据物料代码相同的数据", item1['rawMaterialId'], item2['materialId'])

                # 在materialDictionaries_dict找到item2['materialId']的mainUnitCode
                main_unit_code = [material['mainUnitCode'] for material in materialDictionaries_dict if
                                  material['materialId'] == item2['materialId']][0]
                print("物料主数据物料代码", item2['materialId'], "物料主计量单位", main_unit_code)
                # 在billOfMaterials_dict找到item1['rawMaterialId']的rawMaterialUnitCode
                raw_material_unit_code = [material['rawMaterialUnitCode'] for material in billOfMaterials_dict if
                                          material['rawMaterialId'] == item1['rawMaterialId']][0]
                print("BOM物料代码", item1['rawMaterialId'], "物料在BOM中的计量单位", raw_material_unit_code)

                hasRawMaterialUnitConvert = \
                    [material['hasRawMaterialUnitConvert'] for material in billOfMaterials_dict if
                     material['rawMaterialId'] == item1['rawMaterialId']][0]

                print("BOM中的物料单位转换标记", hasRawMaterialUnitConvert)

                if main_unit_code == raw_material_unit_code and hasRawMaterialUnitConvert == True:
                    print("测试通过")
                    # print("物料单位不需要转换", True)
                elif main_unit_code != raw_material_unit_code and hasRawMaterialUnitConvert == False:
                    # print("物料单位需要转换", False)
                    print("测试通过")
                else:
                    print("测试不通过")

    # # 遍历集合1和集合2
    # for item1 in billOfMaterials_dict:
    #     # print(item1)
    #     for item2 in materialDictionaries_dict:
    #         # print(item2)
    #         # 比较集合2中的materialId与集合1中的productId或rawMaterialId值是否相等
    #         if item2['materialId'] == item1['productId'] or item2['materialId'] == item1['rawMaterialId']:
    #             # 如果相等，就将这个productId或rawMaterialId、materialId值列出来
    #             print(
    #                 f"productId/rawMaterialId: {item1['productId']}/{item1['rawMaterialId']}, materialId: {item2['materialId']}")
