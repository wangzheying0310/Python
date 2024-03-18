# -- coding:utf-8 --
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
        'Client-Identity': '8ff1592731cb56dc10926a2b2229999c',
    }
    response = requests.post('http://172.16.9.2:42010/api/auth/authentication/login', headers=headers, json=payload,
                             verify=False)
    print(response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    print("同步基础数据开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBasicDataForClient_start = time.perf_counter()

    response_synchronizeBasicDataForClient = req.visit("post", "http://172.16.9.2:42010/api/engine/27/scenes/166", json={
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

    print("同步供应链参数开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeDigitalSupplyChainParameterForClient_start = time.perf_counter()

    response_synchronizeDigitalSupplyChainParameterForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/27/scenes/166", json={
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
    response_analyse_start = req.visit("post", 'http://172.16.9.2:42010/api/engine/call/27/166/analyse/start',
                                       headers=headers,
                                       verify=False)

    response_synchronizeDigitalSupplyChainStructureForClient = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/27/scenes/166", json={
            "express": "synchronizeDigitalSupplyChainStructureForClient()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeDigitalSupplyChainStructureForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeDigitalSupplyChainStructureForClient = synchronizeDigitalSupplyChainStructureForClient_end - synchronizeDigitalSupplyChainStructureForClient_start
    # 获取请求结果
    response_analyse_result = req.visit("get", 'http://172.16.9.2:42010/api/engine/call/27/166/analyse/result',
                                        headers=headers, verify=False)
    # 将JSON数据转换为字典列表
    data1 = response_analyse_result.json()["data"]
    print(data1)
    with open(f"./analyse_result-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-SCP-XingNeng1-166.csv", 'w', newline='',
              encoding='utf-8') as csvfile:
        fieldnames = ['sceneId', 'className', 'methodName', 'sumDuration', 'times']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data1:
            writer.writerow(row)

    # 结束分析
    response_analyse_end = requests.post('http://172.16.9.2:42010/api/engine/call/27/166/analyse/stop', headers=headers,
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
        req.visit("post", "http://172.16.9.2:42010/api/engine/27/scenes/166", json={
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
        req.visit("post", "http://172.16.9.2:42010/api/engine/27/scenes/166", json={
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
    # 记录同步优化结束时间w
    print("同步优化时间:%.2f min" % capacityPlanningAlgorithm_min)
    # 记录优化结束系统时间
    print("优化结束系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    response_instanceCount = req.visit("get", 'http://172.16.9.2:42010/api/engine/27/scenes/166/instanceCount',
                                       headers=headers, verify=False)
    data = response_instanceCount.json()["data"]
    print(data)

    # 打开一个csv文件，如果不存在则创建
    with open(f"./instanceCount-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-XingNeng1-166.csv", 'w',
              newline='') as csvfile:
        # 创建一个写入器对象
        fieldnames = ['类型', '数量']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 写入数据行
        for key, value in data.items():
            writer.writerow({'类型': key, '数量': value})