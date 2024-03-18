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
    # 请求库存
    KTInventory = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE:Model03:27/kts/com.aps.model.dm.KTInventory",
                  json={}, headers=headers).json()["data"]

    print(KTInventory)
    KTInventory_len = len(KTInventory)

    # 统计知识表中库存个数
    print('库存知识表数据个数为', KTInventory_len)

    # 请求采购申请
    KTPurchaseRequest = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE:Model03:27/kts/com.aps.model.dm.KTPurchaseRequest",
                  json={}, headers=headers).json()["data"]

    KTPurchaseRequest_len = len(KTPurchaseRequest)
    # print(ProductionVersion)
    print('采购申请知识表数据个数为', KTPurchaseRequest_len)

    # 请求月度发货
    KTMonthlyDelivery = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE:Model03:27/kts/com.aps.model.dm.KTMonthlyDelivery",
                  json={}, headers=headers).json()["data"]

    # print(MaterialDictionary)
    KTMonthlyDelivery_len = len(KTMonthlyDelivery)
    print('月度发货知识表数据个数为', KTMonthlyDelivery_len)

    # 请求采购订单
    KTPurchaseOrder = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE:Model03:27/kts/com.aps.model.dm.KTPurchaseOrder",
                  json={}, headers=headers).json()["data"]

    # print(PointedSupplier)
    KTPurchaseOrder_len = len(KTPurchaseOrder)
    print('采购订单知识表数据个数为', KTPurchaseOrder_len)

    # 点击同步业务数据按钮
    synchronizeBusinessDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeBusinessDataForClient',
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
                          'computeExprs': {},
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

    if deliverySource_dict['total'] == KTMonthlyDelivery_len and inventorySource_dict['total'] == KTInventory_len and \
            purchaseOrderSource_dict['total'] == KTPurchaseOrder_len and purchaseRequestSource_dict[
        'total'] == KTPurchaseRequest_len:
        print("数量相同，测试通过")
    else:
        print("测试未通过")
