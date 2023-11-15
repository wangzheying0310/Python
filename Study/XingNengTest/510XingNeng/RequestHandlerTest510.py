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

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    checkDMSceneState_start = time.perf_counter()

    print(req.visit("post", "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model02/companion-method", json={
        "type": "SupplyChainPlanner",
        "name": "checkDMSceneState",
        "args": [],
        "userNo": "WZY"
    }, headers=headers).json()["data"])
    checkDMSceneState_end = time.perf_counter()

    checkDMSceneState = checkDMSceneState_end - checkDMSceneState_start
    # 打印时长
    print("同步SCP基础数据时间:%.2f s" % checkDMSceneState)
    # 换算成min
    checkDMSceneState_min = checkDMSceneState / 60
    # 打印min
    print("同步SCP基础数据时间:%.2f min" % checkDMSceneState_min)

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