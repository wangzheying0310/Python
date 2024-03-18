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

    #把Model03变为可修改的参数
    # def get_url(model_name):
    #     base_url = "http://172.16.5.10/apim/v2/branch/model/dataManager/%E5%9F%BA%E7%A1%80%E6%95%B0%E6%8D%AE:"
    #     return base_url + model_name + ":36/kts/com.aps.model.dm.KTBillOfMaterial"
    #
    #
    # # 使用新的模型名称调用函数
    # new_url = get_url("Model03")
    # print(new_url)
    # 请求库存
    KTSalesOrder = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E9%9C%80%E6%B1%82%E6%95%B0%E6%8D%AE:Model03:19/kts/com.aps.model.dm.KTSalesOrder",
                  json={}, headers=headers).json()["data"]

    # print(KTSalesOrder)
    KTSalesOrder_len = len(KTSalesOrder)

    # 统计知识表中库存个数
    print('销售订单知识表数据个数为', KTSalesOrder_len)

    # 点击同步销售订单数据按钮
    synchronizeBusinessDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeSalesDataForClient',
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

    print(SalesOrderInDM_dict['total'])

    if SalesOrderInDM_dict['total'] == KTSalesOrder_len:
        print("数量相同，测试通过")
    else:
        print("测试未通过")
