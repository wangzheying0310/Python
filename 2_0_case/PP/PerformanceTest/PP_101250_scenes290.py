# -- coding:utf-8 --
import csv
from datetime import datetime

import requests
import time


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
        'Client-Identity': '8ff1592731cb56dc10926a2b2229999c',
    }
    response = requests.post('http://172.16.9.2:42010/api/auth/authentication/login', headers=headers, json=payload,
                             verify=False)

    print(response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    print("同步业务规则开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBusinessRuleFromKTForClient_start = time.perf_counter()

    response_synchronizeBusinessRuleFromKTForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/26/scenes/290", json={
            "express": "synchronizeBusinessRuleFromKTForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeBusinessRuleFromKTForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeBusinessRuleFromKTForClient = synchronizeBusinessRuleFromKTForClient_end - synchronizeBusinessRuleFromKTForClient_start
    # 打印时长
    print("同步业务规则时间:%.2f s" % synchronizeBusinessRuleFromKTForClient)
    # 换算成min
    synchronizeBusinessRuleFromKTForClient_min = synchronizeBusinessRuleFromKTForClient / 60
    # 打印min
    print("同步业务规则时间:%.2f min" % synchronizeBusinessRuleFromKTForClient_min)

    print("同步PP订单开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeWorkOrdersFromKTForClient_start = time.perf_counter()

    response_synchronizeWorkOrdersFromKTForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/26/scenes/290", json={
            "express": "synchronizeWorkOrdersFromKTForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeWorkOrdersFromKTForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeWorkOrdersFromKTForClient = synchronizeWorkOrdersFromKTForClient_end - synchronizeWorkOrdersFromKTForClient_start
    # 打印时长
    print("同步PP订单时间:%.2f s" % synchronizeWorkOrdersFromKTForClient)
    # 换算成min
    synchronizeWorkOrdersFromKTForClient_min = synchronizeWorkOrdersFromKTForClient / 60
    # 打印min
    print("同步PP订单时间:%.2f min" % synchronizeWorkOrdersFromKTForClient_min)
    # print(synchronizeBasicDataForClient)
    print("同步批次拆解系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBusinessDataForClient_start = time.perf_counter()
    print("开启调用分析")
    # 开启调用分析
    response_analyse_start = requests.post('http://172.16.9.2:42010/api/engine/call/26/290/analyse/start', headers=headers, verify=False)
    print(response_analyse_start.status_code)
    # 点击批次拆解
    response_synchronizeBusinessDataForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/26/scenes/290", json={
            "express": "synchronizeBusinessDataForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeBusinessDataForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeBusinessDataForClient = synchronizeBusinessDataForClient_end - synchronizeBusinessDataForClient_start

    # 获取请求结果
    response_analyse_result = requests.get('http://172.16.9.2:42010/api/engine/call/26/290/analyse/result', headers=headers, verify=False)
    # 将JSON数据转换为字典列表
    data1 = response_analyse_result.json()["data"]

    print(data1)

    with open(f"./analyse_result-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-PP-101250-290.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['sceneId', 'className', 'methodName', 'sumDuration', 'times']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data1:
            writer.writerow(row)

    # 结束分析
    response_analyse_end = requests.post('http://172.16.9.2:42010/api/engine/call/26/290/analyse/stop', headers=headers, verify=False)
    # 打印时长
    print("同步批次拆解时间:%.2f s" % synchronizeBusinessDataForClient)
    # 换算成min
    synchronizeBusinessDataForClient_min = synchronizeBusinessDataForClient / 60
    # 记录同步数字供应链结束时间
    print("同步批次拆解时间:%.2f min" % synchronizeBusinessDataForClient_min)

    print("排程开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeAssignmentForClient_start = time.perf_counter()
    # 发送请求
    response_synchronizeAssignmentForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/26/scenes/290", json={
            "express": "synchronizeAssignmentForClient()"
        }, headers=headers, verify=False).json()["data"]

    # 记录销售需求结束时间
    synchronizeAssignmentForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeAssignmentForClient = synchronizeAssignmentForClient_end - synchronizeAssignmentForClient_start
    # 打印时长
    print("排程时间:%.2f s" % synchronizeAssignmentForClient)
    # 换算成min
    synchronizeAssignmentForClient_min = synchronizeAssignmentForClient / 60

    print("排程时间:%.2f min" % synchronizeAssignmentForClient_min)

    response_instanceCount = req.visit("get", 'http://172.16.9.2:42010/api/engine/26/scenes/290/instanceCount',
                                       headers=headers, verify=False)
    data = response_instanceCount.json()["data"]
    print(data)

    # 打开一个csv文件，如果不存在则创建
    with open(f"./instanceCount-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-13500_290.csv", 'w',
              newline='') as csvfile:
        # 创建一个写入器对象
        fieldnames = ['类型', '数量']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 写入数据行
        for key, value in data.items():
            writer.writerow({'类型': key, '数量': value})



