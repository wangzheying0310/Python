# -- coding:utf-8 --
import time

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
    response = requests.post('http://172.16.5.10/apim/v2/auth/login', headers=headers, json=payload,
                             verify=False)
    print("访问状态码", response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print("token", token)

    TimeInterval_response = req.visit("post",
                                      "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                      json={
                                          'TimeInterval': {
                                              'condition': '',
                                              'sort': '',
                                              'computeExprs': {},
                                              '__page': {
                                                  'num': 1,
                                                  'size': 300,
                                              },
                                          },
                                      }, headers=headers).json()["data"]

    TimeInterval_dict = TimeInterval_response['TimeInterval']

    TimeInterval_list = TimeInterval_dict['rows']

    print(TimeInterval_list)

    HolidayCalendarRule_start = [item['start'] for item in TimeInterval_list if
                                 "HolidayCalendarRule" in item['comment']]

    HolidayCalendarRule_end = [item['end'] for item in TimeInterval_list if "HolidayCalendarRule" in item['comment']]

    # print(HolidayCalendarRule_start, HolidayCalendarRule_end)

    # 将时间转换为只包含时分秒的格式
    formatted_start = [time.strftime('%H:%M:%S', time.strptime(start, '%Y-%m-%d %H:%M:%S')) for start in
                       HolidayCalendarRule_start]
    formatted_end = [time.strftime('%H:%M:%S', time.strptime(end, '%Y-%m-%d %H:%M:%S')) for end in
                     HolidayCalendarRule_end]

    print(formatted_start, formatted_end)



