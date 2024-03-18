# -- coding:utf-8 --
import requests
from datetime import datetime, timedelta


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

    PeriodDefinition_response = req.visit("post",
                             "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                             json={
                                 'PeriodDefinition': {
                                     'condition': '',
                                     'sort': '',
                                     'computeExprs': {},
                                     '__page': {
                                         'num': 1,
                                         'size': 300,
                                     },
                                 },
                             }, headers=headers).json()["data"]

    PeriodDefinition_dict = PeriodDefinition_response['PeriodDefinition']

    PeriodDefinition_list = PeriodDefinition_dict['rows']

    print(PeriodDefinition_list)

    historyLength = [item['historyLength'] for item in PeriodDefinition_list][0]
    print('历史存储时间', historyLength)

    futureLength = [item['futureLength'] for item in PeriodDefinition_list][0]
    print('未来存储时间', futureLength)

    PeriodDefinition = historyLength + futureLength

    print(PeriodDefinition)

    Period_response = req.visit("post",
                                          "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                          json={
                                              'Period': {
                                                  'condition': '',
                                                  'sort': '',
                                                  'computeExprs': {},
                                                  '__page': {
                                                      'num': 1,
                                                      'size': 300,
                                                  },
                                              },
                                          }, headers=headers).json()["data"]

    Period_dict = Period_response['Period']

    Period_num = Period_dict['total']

    print(Period_num)

    if PeriodDefinition + 1 == Period_num:
        print("测试通过")
    else:
        print("测试不通过")
