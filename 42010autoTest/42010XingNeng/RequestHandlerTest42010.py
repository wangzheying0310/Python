import json
import csv
import requests
import time
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
    # print(response.headers)
    print(response.status_code)
    # print(response.text)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    print("同步基础数据开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBasicDataForClient_start = time.perf_counter()

    response_synchronizeBasicDataForClient = req.visit("post", "http://172.16.9.2:42010/api/engine/4/scenes/12", json={
        "express": "synchronizeBasicDataForClient()"
    }, headers=headers, verify=False).json()["data"]

    synchronizeBasicDataForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeBasicDataForClient = synchronizeBasicDataForClient_end - synchronizeBasicDataForClient_start
    # 打印时长
    print("同步基础数据时间:%.2f s" % synchronizeBasicDataForClient)
    # 换算成min
    synchronizeBasicDataForClient_min = synchronizeBasicDataForClient / 60
    # 打印min
    print("同步基础数据时间:%.2f min" % synchronizeBasicDataForClient_min)
    # print(synchronizeBasicDataForClient)
    # print("同步基础数据结束系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    print("同步供应链参数开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeDigitalSupplyChainParameterForClient_start = time.perf_counter()

    response_synchronizeDigitalSupplyChainParameterForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/4/scenes/12", json={
            "express": "synchronizeDigitalSupplyChainParameterForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeDigitalSupplyChainParameterForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeDigitalSupplyChainParameterForClient = synchronizeDigitalSupplyChainParameterForClient_end - synchronizeDigitalSupplyChainParameterForClient_start
    # 打印时长
    print("同步供应链参数时间:%.2f s" % synchronizeDigitalSupplyChainParameterForClient)
    # 换算成min
    synchronizeDigitalSupplyChainParameterForClient_min = synchronizeDigitalSupplyChainParameterForClient / 60
    # 打印min
    print("同步供应链参数时间:%.2f min" % synchronizeDigitalSupplyChainParameterForClient_min)
    # print(synchronizeBasicDataForClient)
    print("同步数字供应链开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeDigitalSupplyChainStructureForClient_start = time.perf_counter()

    # 开启调用分析
    response_analyse_start = req.visit("post", 'http://172.16.9.2:42010/api/engine/call/4/12/analyse/start',
                                       headers=headers,
                                       verify=False)

    response_synchronizeDigitalSupplyChainStructureForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/4/scenes/12", json={
            "express": "synchronizeDigitalSupplyChainStructureForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeDigitalSupplyChainStructureForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeDigitalSupplyChainStructureForClient = synchronizeDigitalSupplyChainStructureForClient_end - synchronizeDigitalSupplyChainStructureForClient_start

    # with open(f"./data-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}.json", 'w') as f:
    # 获取请求结果
    response_analyse_result = req.visit("get", 'http://172.16.9.2:42010/api/engine/call/4/12/analyse/result',
                                        headers=headers, verify=False)
    data = response_analyse_result.json()["data"]

    try:
        with open(f"./analyse_result-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-XingNeng2.csv", 'w', newline='',
                  encoding='utf-8') as f:
            # csv.DictWriter()是一个用于将字典列表写入CSV文件的类。它接受两个参数：第一个参数是要写入的文件对象，第二个参数是字段名列表。
            # fieldnames=data[0].keys()表示从data列表的第一个元素（假设它是一个字典）中获取所有的键作为字段名。
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            # writer.writeheader()方法用于将字段名写入CSV文件的第一行，作为表头。
            writer.writeheader()
            # 循环遍历data列表中的每个字典元素，将其作为一行数据写入CSV文件。
            for row in data:
                try:
                    # 将字典row写入CSV文件的下一行
                    writer.writerow(row)
                except IndexError as e:
                    print(f"发生错误：{e}")
                    continue
    except Exception as e:
        print(f"发生错误：{e}")

    # 结束分析
    response_analyse_end = requests.post('http://172.16.9.2:42010/api/engine/call/4/12/analyse/stop', headers=headers,
                                         verify=False)
    # 打印时长
    print("同步数字供应链时间:%.2f s" % synchronizeDigitalSupplyChainStructureForClient)
    # 换算成min
    synchronizeDigitalSupplyChainStructureForClient_min = synchronizeDigitalSupplyChainStructureForClient / 60
    # 记录同步数字供应链结束时间
    print("同步数字供应链时间:%.2f min" % synchronizeDigitalSupplyChainStructureForClient_min)

    print("同步销售需求开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeSalesDataForClient_start = time.perf_counter()
    # 发送请求
    response_synchronizeSalesDataForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/4/scenes/12", json={
            "express": "synchronizeSalesDataForClient()"
        }, headers=headers, verify=False).json()["data"]
    # 记录销售需求结束时间
    synchronizeSalesDataForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeSalesDataForClient = synchronizeSalesDataForClient_end - synchronizeSalesDataForClient_start
    # 打印时长
    print("同步销售需求时间:%.2f s" % synchronizeSalesDataForClient)
    # 换算成min
    synchronizeSalesDataForClient_min = synchronizeSalesDataForClient / 60

    print("同步销售需求时间:%.2f min" % synchronizeSalesDataForClient_min)

    print("优化开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    # 记录优化开始时间
    capacityPlanningAlgorithm_start = time.perf_counter()
    # 发送请求
    response_capacityPlanningAlgorithm = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/4/scenes/12", json={
            "express": "algorithm.capacityPlanningAlgorithm()"
        }, headers=headers, verify=False).json()["data"]
    # 记录优化结束时间
    capacityPlanningAlgorithm_end = time.perf_counter()
    # 计算总时长
    capacityPlanningAlgorithm = capacityPlanningAlgorithm_end - capacityPlanningAlgorithm_start
    # 打印时长
    print("同步优化时间:%.2f s" % capacityPlanningAlgorithm)
    # 换算成min
    capacityPlanningAlgorithm_min = capacityPlanningAlgorithm / 60
    # 记录同步优化结束时间
    print("同步优化时间:%.2f min" % capacityPlanningAlgorithm_min)
    # 记录优化结束系统时间
    print("优化结束系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


