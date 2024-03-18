# -- coding:utf-8 --
import requests
from datetime import datetime


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

    # print(TimeInterval_list)
    TimeInterval_start = [item['start'] for item in TimeInterval_list if "HolidayCalendarRule" not in item['comment']]
    print('停机开始时间集合', TimeInterval_start)

    TimeInterval_end = [item['end'] for item in TimeInterval_list if "HolidayCalendarRule" not in item['comment']]
    print('停机结束时间集合', TimeInterval_end)

    CalendarRule_response = req.visit("post",
                                      "http://172.16.5.10/apim/v2/scene/piece-planner/Model03/computeExprDatas",
                                      json={
                                          'CalendarRule': {
                                              'condition': '',
                                              'sort': '',
                                              'computeExprs': {},
                                              '__page': {
                                                  'num': 1,
                                                  'size': 300,
                                              },
                                          },
                                      }, headers=headers).json()["data"]

    CalendarRule_dict = CalendarRule_response['CalendarRule']

    CalendarRule_list = CalendarRule_dict['rows']

    # print(CalendarRule_list)

    CalendarRule_start = [item['start'] for item in CalendarRule_list][0]

    print('规则开始时间', CalendarRule_start)

    CalendarRule_end = [item['end'] for item in CalendarRule_list][0]
    print('规则结束时间', CalendarRule_end)
    # 定义规则开始时间
    start_time = datetime.strptime(CalendarRule_start, '%Y-%m-%d %H:%M:%S')
    # 定义规则结束时间
    end_time = datetime.strptime(CalendarRule_end, '%Y-%m-%d %H:%M:%S')

    # 判断生成的设备日历时间在规则开始时间结束时间之内
    # 创建一个集合
    out_of_range_times = []
    # 遍历所有停机开始时间
    for time_str in TimeInterval_start:
        range_times = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        if start_time <= range_times <= end_time:
            out_of_range_times.append(time_str)

    for time_str in TimeInterval_end:
        range_times = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        if start_time <= range_times <= end_time:
            out_of_range_times.append(time_str)
    if out_of_range_times:
        print("测试通过")
    else:
        print("不在指定时间范围内的时间为：", out_of_range_times)

    # for date_str in TimeInterval_end:
    #     date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    #     if date_obj.hour == 6 and date_obj.minute == 0 and date_obj.second == 0:
    #         print(f"{date_str} 的时分秒都为 06:00:00")
    #     else:
    #         print(f"{date_str} 的时分秒不全为 06:00:00")
    all_same_six = True
    # 判断停机结束时间是否与知识表一致

    for date_str_six in TimeInterval_end:
        date_obj_six = datetime.strptime(date_str_six, '%Y-%m-%d %H:%M:%S')
        # 时间根据需要自己修改
        if date_obj_six.hour != 6 or date_obj_six.minute != 0 or date_obj_six.second != 0:
            all_same_six = False
            break

    if all_same_six:
        print("全部数据都为 06:00:00,测试通过")
    else:
        for date_str_six in TimeInterval_end:
            date_obj_six = datetime.strptime(date_str_six, '%Y-%m-%d %H:%M:%S')
            if date_obj_six.hour == 6 and date_obj_six.minute == 0 and date_obj_six.second == 0:
                print(f"{date_str_six} 的时分秒都为 06:00:00")
            else:
                print(f"{date_str_six} 的时分秒不全为 06:00:00")
    # for date_str in TimeInterval_start :
    #     date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    #     if date_obj.hour == 6 and date_obj.minute == 0 and date_obj.second == 0:
    #         print(f"{date_str} 的时分秒都为 06:00:00")
    #     else:
    #         print(f"{date_str} 的时分秒不全为 06:00:00")
    all_same_ten = True
    # 判断停机开始时间是否与知识表一致
    for date_str_ten in TimeInterval_start:
        date_obj_ten = datetime.strptime(date_str_ten, '%Y-%m-%d %H:%M:%S')
        if date_obj_ten.hour != 22 or date_obj_ten.minute != 30 or date_obj_ten.second != 0:
            all_same_ten = False
            break

    if all_same_ten:
        print("全部数据都为 22:30:00,测试通过")
    else:
        for date_str_ten in TimeInterval_start:
            date_obj_ten = datetime.strptime(date_str_ten, '%Y-%m-%d %H:%M:%S')
            if date_obj_ten.hour == 22 and date_obj_ten.minute == 30 and date_obj_ten.second == 0:
                print(f"{date_str_ten} 的时分秒都为 22:30:00")
            else:
                print(f"{date_str_ten} 的时分秒不全为 22:30:00")
