# -- coding:utf-8 --

import requests


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

    token = req.visit("post", url, json=payload, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    PeriodParameter_response = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/supplychain-planner/%E5%9C%BA%E6%99%AF%E5%8F%82%E6%95%B0:Model03:64/kts/com.aps.model.scpm.KTPeriodParameter",
                  headers=headers).json()["data"]

    # print(PeriodParameter_response)

    number_of_frozen_period = PeriodParameter_response[0]['numberOfFrozenPeriod']
    print("冻结周期数", number_of_frozen_period)

    updata_frozen_response = req.visit("post",
                                       'http://172.16.5.10/apim/v2/branch/model/supplychain-planner/%E5%9C%BA%E6%99%AF%E5%8F%82%E6%95%B0:Model03:64/add-kts',
                                       json={
                                           'createUser': 'admin',
                                           'branchName': '模式3',
                                           'remark': '修改冻结周期为3',
                                           'vos': [
                                               {
                                                   'ktIdentity': 'com.aps.model.scpm.KTPeriodParameter',
                                                   'deleteAll': False,
                                                   'deleteIds': [],
                                                   'addRows': [],
                                                   'updateRows': [
                                                       {
                                                           'ktid': 0,
                                                           'firstWeekDay': 'Monday',
                                                           'hasManualSystemTime': True,
                                                           'manualSystemTime': '2023-06-01 00:00:00',
                                                           'numberOfFrozenPeriod': 3,
                                                           'periodsBeforePlanningHorizon': 1,
                                                           'releasePeriodQty': 1,
                                                       },
                                                   ],
                                               },
                                           ],
                                       }, headers=headers).json()["data"]

    PeriodParameter_response = \
        req.visit("get",
                  "http://172.16.5.10/apim/v2/branch/model/supplychain-planner/%E5%9C%BA%E6%99%AF%E5%8F%82%E6%95%B0:Model03:64/kts/com.aps.model.scpm.KTPeriodParameter",
                  headers=headers).json()["data"]

    print(PeriodParameter_response)

    productionLinesOption_response \
        = req.visit("post",
                    "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/data-method",
                    json={
                        'oid': 1275068796,
                        'method': 'manuallySetNewSupplyQuantityByUnit',
                        'args': [
                            '2000',
                            '总量',
                        ],
                        'userNo': 'WZY',
                    }, headers=headers).json()["data"]
    print(productionLinesOption_response)
