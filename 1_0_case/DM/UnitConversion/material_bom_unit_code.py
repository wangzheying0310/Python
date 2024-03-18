# -- coding:utf-8 --
import requests
from request_handler import RequestHandler
import time

# 基础信息全部填写为DB

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
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


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

    print("访问BOM")

    billOfMaterials_response = \
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

    BOM_dict = billOfMaterials_response['HandledBillOfMaterialInDM']

    print(BOM_dict)

    BOM_list = BOM_dict['rows']

    print("BOM集合", BOM_list)

    # 遍历billOfMaterials_dict
    for item1 in BOM_list:

        # 遍历materialDictionaries_dict
        for item2 in materialDictionaries_list:

            # 如果Item1的productId等于Item2的materialId
            if item1['productId'] == item2['materialNr']:

                # 打印Item1的productId和Item2的materialId
                print("BOM产品代码与物料主数据物料代码相同的数据", item1['productId'], item2['materialNr'])

                # 在materialDictionaries_dict找到item2['materialId']的mainUnitCode
                main_unit_code_pro = [product['productUnitCode'] for product in BOM_list if
                                      product['productId'] == item2['materialNr']][0]

                print("BOM产品代码", item1['productId'], "产品主计量单位", main_unit_code_pro)

                raw_material_unit_code_pro = [material['mainUnitCode'] for material in materialDictionaries_list if
                                              item1['productId'] == material['materialNr']][0]

                print("物料主数据产品代码", item2['materialNr'], "产品主计量单位", raw_material_unit_code_pro)

                lackProductUnitConvert = [product['lackProductUnitConvert'] for product in BOM_list if
                                          product['productId'] == item2['materialNr']][0]

                print("BOM中的产品单位转换标记", lackProductUnitConvert)

                if main_unit_code_pro == raw_material_unit_code_pro and lackProductUnitConvert == False:
                    print("测试通过")
                elif main_unit_code_pro != raw_material_unit_code_pro and lackProductUnitConvert == True:
                    print("测试通过")
                else:
                    print("测试不通过")
                    # print("产品单位需要转换", False)

            #     如果item1['rawMaterialId'] == item2['materialId']
            elif item1['rawMaterialId'] == item2['materialNr']:

                # 打印item1['rawMaterialId'], item2['materialId']
                print("BOM物料代码与物料主数据物料代码相同的数据", item1['rawMaterialId'], item2['materialNr'])

                # 在materialDictionaries_dict找到item2['materialId']的mainUnitCode
                main_unit_code = [material['mainUnitCode'] for material in materialDictionaries_list if
                                  material['materialNr'] == item2['materialNr']][0]
                print("物料主数据物料代码", item2['materialNr'], "物料主计量单位", main_unit_code)
                # 在billOfMaterials_dict找到item1['rawMaterialId']的rawMaterialUnitCode
                raw_material_unit_code = [material['rawMaterialUnitCode'] for material in BOM_list if
                                          material['rawMaterialId'] == item1['rawMaterialId']][0]
                print("BOM物料代码", item1['rawMaterialId'], "物料在BOM中的计量单位", raw_material_unit_code)

                lackRawMaterialUnitConvert = \
                    [material['lackRawMaterialUnitConvert'] for material in BOM_list if
                     material['rawMaterialId'] == item1['rawMaterialId']][0]

                print("BOM中的物料单位转换标记", lackRawMaterialUnitConvert)

                if main_unit_code == raw_material_unit_code and lackRawMaterialUnitConvert == False:

                    print("测试通过")

                elif main_unit_code != raw_material_unit_code and lackRawMaterialUnitConvert == True:

                    print("测试通过")

                else:

                    print("测试不通过")
