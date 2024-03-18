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

    Resource_response = req.visit("post",
                                  "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                  json={
                                      'Resource': {
                                          'condition': '',
                                          'sort': '',
                                          'computeExprs': {},
                                          '__page': {
                                              'num': 1,
                                              'size': 300,
                                          },
                                      },
                                  }, headers=headers).json()["data"]

    Resource_dict = Resource_response['Resource']

    Resource_list = Resource_dict['rows']

    # print(Resource_list)

    usedCapacityInHour = [item['usedCapacityInHour'] for item in Resource_list]
    print('可用产能', usedCapacityInHour)
    print("总可用产能", sum(usedCapacityInHour))

    totalProcessDurationInHour = [item['totalProcessDurationInHour'] for item in Resource_list]
    print('已用产能', totalProcessDurationInHour)
    print("总已用产能", sum(totalProcessDurationInHour))

    KPIResourceUtilization = round(sum(totalProcessDurationInHour) / sum(usedCapacityInHour) * 100, 2)
    print(KPIResourceUtilization)

    KPIResourceUtilization_response = req.visit("post",
                                                "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                                json={
                                                    'KPIResourceUtilization': {
                                                        'condition': '',
                                                        'sort': '',
                                                        'computeExprs': {},
                                                        '__page': {
                                                            'num': 1,
                                                            'size': 300,
                                                        },
                                                    },
                                                }, headers=headers).json()["data"]

    KPIResourceUtilization_dict = KPIResourceUtilization_response['KPIResourceUtilization']

    KPIResourceUtilization_list = KPIResourceUtilization_dict['rows']

    # print(KPIResourceUtilization_list)

    ResourceUtilization = [item['value'] for item in KPIResourceUtilization_list][0]
    print('KPI产能利用率', ResourceUtilization)

    if ResourceUtilization == KPIResourceUtilization:
        print("值相等，测试通过")
    else:
        print("值不相等，测试不通过")
