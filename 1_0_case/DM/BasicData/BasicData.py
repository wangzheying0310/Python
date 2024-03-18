import time

from request_handler import RequestHandler

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

    # print(token)
    print('执行时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 请求基础数据知识表中的数据，条数及内容
    # 请求BOM
    BillOfMaterial = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E5%9F%BA%E7%A1%80%E6%95%B0%E6%8D%AE:Model03:36/kts/com.aps.model.dm.KTBillOfMaterial",
                  json={}, headers=headers).json()["data"]

    # print(BillOfMaterial)
    BillOfMaterial_len = len(BillOfMaterial)

    # 统计知识表中BOM个数
    print('BOM知识表数据个数为', BillOfMaterial_len)

    # 请求生产版本
    ProductionVersion = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E5%9F%BA%E7%A1%80%E6%95%B0%E6%8D%AE:Model03:36/kts/com.aps.model.dm.KTProductionVersion",
                  json={}, headers=headers).json()["data"]

    ProductionVersion_len = len(ProductionVersion)
    # print(ProductionVersion)
    print('生产版本知识表数据个数为', ProductionVersion_len)

    # 请求物料主数据
    MaterialDictionary = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E5%9F%BA%E7%A1%80%E6%95%B0%E6%8D%AE:Model03:36/kts/com.aps.model.dm.KTMaterialDictionary",
                  json={}, headers=headers).json()["data"]

    # print(MaterialDictionary)
    MaterialDictionary_len = len(MaterialDictionary)
    print('物料主数据知识表数据个数为', MaterialDictionary_len)

    # 请求指定供应商
    PointedSupplier = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E5%9F%BA%E7%A1%80%E6%95%B0%E6%8D%AE:Model03:36/kts/com.aps.model.dm.KTPointedSupplier",
                  json={}, headers=headers).json()["data"]

    # print(PointedSupplier)
    PointedSupplier_len = len(PointedSupplier)
    print('指定供应商知识表数据个数为', len(PointedSupplier))

    # 点击同步基础数据按钮
    synchronizeBasicDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeBasicDataForClient',
                      'args': [],
                      'userNo': 'WZY',
                  }, headers=headers).json()["data"]
    preHandleDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'preHandleDataForClient',
                      'args': [],
                      'userNo': 'WZY',
                  }, headers=headers).json()["data"]

    # 请求BOM节点数据
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
                              'size': 1000,
                          },
                      },
                  }, headers=headers).json()["data"]

    BOM_dict = BOM_response['HandledBillOfMaterialInDM']

    print('BOM节点数据个数为', BOM_dict['total'])

    # 请求物料主数据节点数据
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
                              'size': 1000,
                          },
                      },
                  }, headers=headers).json()["data"]

    MaterialDictionary_dict = MaterialDictionary_response['MaterialDictionaryInDM']

    print('物料主数据节点数据个数为', MaterialDictionary_dict['total'])

    # 请求生产版本节点数据
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
                              'size': 1000,
                          },
                      },
                  }, headers=headers).json()["data"]

    ProductionVersion_dict = ProductionVersion_response['ProductionVersionInDM']
    # print(ProductionVersion_dict['rows'])

    print('生产版本节点数据个数为', ProductionVersion_dict['total'])

    if BOM_dict['total'] == BillOfMaterial_len and MaterialDictionary_dict['total'] == MaterialDictionary_len and \
            ProductionVersion_dict['total'] == ProductionVersion_len:
        print("数量相同，测试通过")
    else:
        print("测试未通过")
