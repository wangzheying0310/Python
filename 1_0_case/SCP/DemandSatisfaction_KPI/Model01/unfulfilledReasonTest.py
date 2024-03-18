# -- coding:utf-8 --
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

    print(token)

    PISPIP_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model01/computeExprDatas",
                  json={
                      'ProductInStockingPointInPeriod': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 5000,
                          },
                      },
                  }, headers=headers).json()["data"]

    ProductInStockingPointInPeriod_dict = PISPIP_response['ProductInStockingPointInPeriod']

    unfulfilledReason_list = [row['unfulfilledReason'] for row in ProductInStockingPointInPeriod_dict['rows'] if
                              row['unfulfilledReason'] != '']

    print(unfulfilledReason_list)
    print("不满足原因个数", len(unfulfilledReason_list))

    allUnfulfilledDemandQuantityForOG_list = [row['allUnfulfilledDemandQuantityForOG'] for row in
                                              ProductInStockingPointInPeriod_dict['rows'] if
                                              row['allUnfulfilledDemandQuantityForOG'] != 0]

    print(allUnfulfilledDemandQuantityForOG_list)
    print("不满足量个数", len(allUnfulfilledDemandQuantityForOG_list))

    if len(unfulfilledReason_list) == len(allUnfulfilledDemandQuantityForOG_list):
        print("测试通过")
    else:
        print("存在有未满足量但无满足原因情况")