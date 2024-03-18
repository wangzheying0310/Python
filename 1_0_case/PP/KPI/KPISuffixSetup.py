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

    Ass_response = req.visit("post",
                             "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                             json={
                                 'Assignment': {
                                     'condition': '',
                                     'sort': '',
                                     'computeExprs': {},
                                     '__page': {
                                         'num': 1,
                                         'size': 300,
                                     },
                                 },
                             }, headers=headers).json()["data"]

    Ass_dict = Ass_response['Assignment']

    Ass_list = Ass_dict['rows']

    # print(Ass_list)


    def convert_to_hours(time_list):
        total_seconds = 0
        for time_str in time_list:
            hours, minutes, seconds = map(int, time_str.split(':'))
            total_seconds += timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()
        return total_seconds / 3600


    Data = [item['suffixDuration'] for item in Ass_list]
    print('后处理时间元组', Data)

    SuffixSetup = convert_to_hours(Data)
    print('后处理时间和', SuffixSetup)

    KPISuffixSetup_response = req.visit("post",
                                        "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                        json={
                                            'KPISuffixSetup': {
                                                'condition': '',
                                                'sort': '',
                                                'computeExprs': {},
                                                '__page': {
                                                    'num': 1,
                                                    'size': 300,
                                                },
                                            },
                                        }, headers=headers).json()["data"]

    KPISuffixSetup_dict = KPISuffixSetup_response['KPISuffixSetup']

    KPISuffixSetup_list = KPISuffixSetup_dict['rows']

    # print(KPIResourceUtilization_list)

    KPISuffixSetup = [item['value'] for item in KPISuffixSetup_list][0]
    print('后处理时间值', KPISuffixSetup)

    if KPISuffixSetup == SuffixSetup:
        print('值相等，测试通过')
    else:
        print('值不相等，测试不通过')
