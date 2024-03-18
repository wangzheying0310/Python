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

    print("同步基础数据开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBasicData_start = time.perf_counter()

    response_synchronizeBasicData = req.visit("post", "http://172.16.9.2:42010/api/engine/25/scenes/282", json={
        "express": "synchronizeBasicData()"
    }, headers=headers, verify=False).json()["data"]

    synchronizeBasicData_end = time.perf_counter()
    # 计算总时长
    synchronizeBasicData = synchronizeBasicData_end - synchronizeBasicData_start
    # 打印时长
    print("同步基础数据时间:%.2f s" % synchronizeBasicData)
    # 换算成min
    synchronizeBasicData_min = synchronizeBasicData / 60
    # 打印min
    print("同步基础数据时间:%.2f min" % synchronizeBasicData_min)

    print("同步业务数据时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBusinessData_start = time.perf_counter()

    response_synchronizeBusinessData = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/25/scenes/282", json={
            "express": "synchronizeBusinessData()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeBusinessData_end = time.perf_counter()
    # 计算总时长
    synchronizeBusinessData = synchronizeBusinessData_end - synchronizeBusinessData_start
    # 打印时长
    print("同步业务数据时间:%.2f s" % synchronizeBusinessData)
    # 换算成min
    synchronizeBusinessData_min = synchronizeBusinessData / 60
    # 打印min
    print("同步业务数据时间:%.2f min" % synchronizeBusinessData_min)

    print("同步销售需求开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeSalesData_start = time.perf_counter()

    response_synchronizeSalesData = \
        req.visit("post", "http://172.16.9.2:42010/api/engine/25/scenes/282", json={
            "express": "synchronizeSalesData()"
        }, headers=headers, verify=False).json()["data"]

    synchronizeSalesData_end = time.perf_counter()
    # 计算总时长
    synchronizeSalesData = synchronizeSalesData_end - synchronizeSalesData_start

    # 打印时长
    print("同步销售需求时间:%.2f s" % synchronizeSalesData)
    # 换算成min
    synchronizeSalesData_min = synchronizeSalesData / 60
    # 记录同步数字供应链结束时间
    print("同步销售需求时间:%.2f min" % synchronizeSalesData_min)

    response_instanceCount = req.visit("get", 'http://172.16.9.2:42010/api/engine/25/scenes/282/instanceCount',
                                       headers=headers, verify=False)
    data = response_instanceCount.json()["data"]
    print(data)

    # 打开一个csv文件，如果不存在则创建
    with open(f"./instanceCount-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-XingNeng2DM_282.csv", 'w',
              newline='') as csvfile:
        # 创建一个写入器对象
        fieldnames = ['类型', '数量']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 写入数据行
        for key, value in data.items():
            writer.writerow({'类型': key, '数量': value})



