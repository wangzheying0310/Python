# -- coding:utf-8 --
import time
from request_handler import RequestHandler
# 销售信息全部填写为HTTP

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
    print('执行时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    KT_SalesDataSource_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/branch/model/dataManager/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0:Model03:29/add-kts",
                  json={
                      'createUser': 'WZY',
                      'branchName': '模式3',
                      'remark': '修改为HTTP',
                      'vos': [
                          {
                              'ktIdentity': 'com.aps.model.dm.KTSalesDataSource',
                              'deleteAll': False,
                              'deleteIds': [],
                              'addRows': [],
                              'updateRows': [
                                  {
                                      'ktid': 0,
                                      'orderRemainSource': 'HTTP',
                                      'salesOrderSource': 'HTTP',
                                  },
                              ],
                          },
                      ],
                  }, headers=headers).json()["data"]

    print(KT_SalesDataSource_response)

    synchronizeSalesDataForClient_response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/companion-method",
                  json={
                      'type': 'DataManager',
                      'name': 'synchronizeSalesDataForClient',
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

    if SalesOrderInDM_dict['total'] == 0:
        print("未获取到数据，测试通过")
    else:
        print("测试未通过")
