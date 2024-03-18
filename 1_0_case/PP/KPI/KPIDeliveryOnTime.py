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

    Piece_response = req.visit("post",
                               "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                               json={
                                   'Piece': {
                                       'condition': '',
                                       'sort': '',
                                       'computeExprs': {},
                                       '__page': {
                                           'num': 1,
                                           'size': 300,
                                       },
                                   },
                               }, headers=headers).json()["data"]

    Piece_dict = Piece_response['Piece']

    Piece_list = Piece_dict['rows']

    # print(Piece_list)

    isScheduledOnTime = [item['isScheduledOnTime'] for item in Piece_list]
    # print('是否按时完成', isScheduledOnTime)

    isScheduledOnTime_result = [item['pieceSizeQuantity'] for item in Piece_list if item['isScheduledOnTime']]

    print('所有按时满足产品批数数量和', sum(isScheduledOnTime_result))

    result = [item['pieceSizeQuantity'] for item in Piece_list]
    print('所有产品批数数量和', sum(result))

    DeliveryOnTime = round(sum(isScheduledOnTime_result) / sum(result) * 100, 2)
    print(DeliveryOnTime)

    KPIDeliveryOnTime_response = req.visit("post",
                                           "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                           json={
                                               'KPIDeliveryOnTime': {
                                                   'condition': '',
                                                   'sort': '',
                                                   'computeExprs': {},
                                                   '__page': {
                                                       'num': 1,
                                                       'size': 300,
                                                   },
                                               },
                                           }, headers=headers).json()["data"]

    KPIDeliveryOnTime_dict = KPIDeliveryOnTime_response['KPIDeliveryOnTime']

    KPIDeliveryOnTime_list = KPIDeliveryOnTime_dict['rows']

    # print(KPIResourceUtilization_list)

    KPIDeliveryOnTime = [item['value'] for item in KPIDeliveryOnTime_list][0]
    print('KPI按时交付率', KPIDeliveryOnTime)

    if KPIDeliveryOnTime == DeliveryOnTime:
        print('值相等，测试通过')
    else:
        print('值不相等，测试不通过')
