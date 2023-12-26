# -- coding:utf-8 --
import requests


# 业务数据来自DB


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

    print(response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    print("修改")
    update_response = req.visit("post", "http://172.16.9.2:42010/api/engine/projects/2/table/data", json={
        'express': '系统参数\uffffModel03\uffff14',
        'codeVersionId': '143',
        'remark': '修改业务数据为DB',
        'operators': [
            {
                'tableName': 'KTBusinessDataSource',
                'addRows': [],
                'updateRows': [
                    {
                        'tid': '2721819',
                        'row': {
                            'inventorySource': 'DB',
                            'purchaseOrderSource': 'DB',
                            'purchaseRequestSource': 'DB',
                            'deliverySource': 'DB',
                        },
                    },
                ],
                'deleteIds': [],
                'deleteAll': False,
            },
        ],
    }, headers=headers, verify=False).json()["data"]

    print(update_response)

    print("发送重启场景请求")

    restart_response = requests.put('http://172.16.9.2:42010/api/engine/2/scenes/restart/170', headers=headers,
                                    verify=False)

    print(restart_response)

    print("点击同步业务数据")

    synchronizeBasicData_response = req.visit("post", "http://172.16.9.2:42010/api/engine/2/scenes/170", json={
        'express': 'synchronizeBusinessData()',
    }, headers=headers, verify=False).json()["data"]

    print("打开库存")

    Invent_response = req.visit("post",
                                "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                json={
                                    'express': 'inventories',
                                }, headers=headers).json()["data"]

    print("库存数据个数：", Invent_response['count'])

    print("打开采购订单")

    purchaseOrder_response = req.visit("post",
                                       "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                       json={
                                           'express': 'purchaseOrders',
                                       }, headers=headers).json()["data"]

    print("采购订单个数：", purchaseOrder_response['count'])

    print("打开采购申请")

    purchaseRequest_response = req.visit("post",
                                         "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                         json={
                                             'express': 'purchaseRequests',
                                         }, headers=headers).json()["data"]

    print("采购申请个数：", purchaseRequest_response['count'])

    deliver_response = req.visit("post",
                                 "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                 json={
                                     'express': 'deliveries',
                                 }, headers=headers).json()["data"]

    print("月度发货个数：", deliver_response['count'])

    print("计算库存、采购订单、采购申请、月度发货个数")

    if Invent_response['count'] == purchaseOrder_response['count'] == purchaseRequest_response['count'] == deliver_response['count'] == 0:
        print("未获取到数据，测试通过")
    else:
        print("测试未通过")
