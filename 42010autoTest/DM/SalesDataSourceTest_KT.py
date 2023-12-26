# -- coding:utf-8 --
import requests


# 销售数据来自KT


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
        'express': '系统参数\uffffXingNeng\uffff1',
        'codeVersionId': '143',
        'remark': '销售数据全部修改为KT',
        'operators': [
            {
                'tableName': 'KTSalesDataSource',
                'addRows': [],
                'updateRows': [
                    {
                        'tid': '2005164',
                        'row': {
                            'salesOrderSource': 'KT',
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

    print("点击同步销售数据")

    synchronizeBasicData_response = req.visit("post", "http://172.16.9.2:42010/api/engine/2/scenes/170", json={
        'express': 'synchronizeSalesData()',
    }, headers=headers, verify=False).json()["data"]

    print("打开销售订单")

    salesOrder_response = req.visit("post",
                                    "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                    json={
                                        'express': 'salesOrders',
                                    }, headers=headers).json()["data"]

    print("订单数据个数：", salesOrder_response['count'])

    print("计算销售订单个数")

    if salesOrder_response['count'] != 0:
        print("获取到数据，测试通过")
    else:
        print("测试未通过")
