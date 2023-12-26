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

    print("同步业务规则开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    checkDMSceneState_start = time.perf_counter()

    response_checkDMSceneState = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "checkDMSceneState",
            "args": [],
            "userNo": "WZY"
        }, headers=headers).json()["data"]

    response_synchronizeBusinessRuleForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "synchronizeBusinessRuleForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers).json()["data"]
    print(response_checkDMSceneState)

    checkDMSceneState_end = time.perf_counter()
    # 计算总时长
    checkDMSceneState = checkDMSceneState_end - checkDMSceneState_start
    # 打印时长
    print("同步业务规则时间:%.2f s" % checkDMSceneState)
    # 换算成min
    checkDMSceneState_min = checkDMSceneState / 60
    # 打印min
    print("同步业务规则时间:%.2f min" % checkDMSceneState_min)

    print("同步订单开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeWorkOrderForClient_start = time.perf_counter()

    response_synchronizeWorkOrderForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "synchronizeWorkOrderForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    response_SynchronizationFromKT = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "SynchronizationFromKT",
            "name": "synchronizeWorkOrderForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    response_synchronizeDevelopOccupyForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "synchronizeDevelopOccupyForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    synchronizeWorkOrderForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeWorkOrderForClient = synchronizeWorkOrderForClient_end - synchronizeWorkOrderForClient_start
    # 打印时长
    print("同步订单时间:%.2f s" % synchronizeWorkOrderForClient)
    # 换算成min
    synchronizeWorkOrderForClient_min = synchronizeWorkOrderForClient / 60
    # 打印min
    print("同步订单时间:%.2f min" % synchronizeWorkOrderForClient)

    print("同步批次拆解开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBusinessDataForClient_start = time.perf_counter()

    # 开启调用分析
    response_analyse_start = req.visit("post",
                                       'http://172.16.5.10/api/v1/performance/piece-planner/XingNeng/startCollect',
                                       headers=headers,
                                       verify=False)

    response_synchronizeBusinessDataForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "synchronizeBusinessDataForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    synchronizeBusinessDataForClient_end = time.perf_counter()

    # 计算总时长
    synchronizeBusinessDataForClient = synchronizeBusinessDataForClient_end - synchronizeBusinessDataForClient_start

    # 获取请求结果
    response_analyse_result = req.visit("get",
                                        'http://172.16.5.10/api/v1/performance/piece-planner/XingNeng/callAnalysis',
                                        headers=headers, verify=False)
    # 将JSON数据转换为字典列表
    data = response_analyse_result.json()["data"]
    # 将字典列表写入CSV文件
    """open()函数用于打开一个文件，并返回一个文件对象
    在这里，它被用来创建一个名为data-<当前时间>.csv的文件，其中<当前时间>是使用datetime.now().strftime('%Y,%m,%d %H-%M-%S')格式化得到的字符串
    'w'参数表示以写入模式打开文件，如果文件不存在则创建新文件
    newline=''参数用于确保在不同操作系统上换行符的正确处理
    encoding='utf-8'参数指定了文件的编码格式为UTF-8"""

    try:
        with open(f"./analyse_result-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}-510XingNengPP.csv", 'w', newline='',
                  encoding='utf-8') as f:
            # csv.DictWriter()是一个用于将字典列表写入CSV文件的类。它接受两个参数：第一个参数是要写入的文件对象，第二个参数是字段名列表。
            # fieldnames=data[0].keys()表示从data列表的第一个元素（假设它是一个字典）中获取所有的键作为字段名。
            writer = csv.DictWriter(f, fieldnames=data.keys())
            # writer.writeheader()方法用于将字段名写入CSV文件的第一行，作为表头。
            writer.writeheader()
            # 循环遍历data列表中的每个字典元素，将其作为一行数据写入CSV文件。
            writer = csv.writer(f)
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
    response_analyse_end = requests.post(
        'http://172.16.5.10/api/v1/performance/piece-planner/XingNeng/endCollect', headers=headers,
        verify=False)
    # 打印时长
    print("同步批次拆解时间:%.2f s" % synchronizeBusinessDataForClient)
    # 换算成min
    synchronizeBusinessDataForClient_min = synchronizeBusinessDataForClient / 60
    # 记录同步数字供应链结束时间
    print("同步批次拆解时间:%.2f min" % synchronizeBusinessDataForClient_min)

    print("同步排程开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    planWorkOrderAndOptimizeForClient_start = time.perf_counter()
    # 发送请求
    response_planWorkOrderAndOptimizeForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
            "type": "PiecePlanner",
            "name": "planWorkOrderAndOptimizeForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    # response_sendTestOrderToDMForClient = \
    #     req.visit("post", "http://172.16.5.10/apim/v2/scene/piece-planner/XingNeng/companion-method", json={
    #         "type": "PiecePlanner",
    #         "name": "sendTestOrderToDMForClient",
    #         "args": [],
    #         "userNo": "WZY"
    #     }, headers=headers, verify=False).json()["data"]

    # 记录销售需求结束时间
    planWorkOrderAndOptimizeForClient_end = time.perf_counter()
    # 计算总时长
    planWorkOrderAndOptimizeForClient = planWorkOrderAndOptimizeForClient_end - planWorkOrderAndOptimizeForClient_start
    # 打印时长
    print("同步排程时间:%.2f s" % planWorkOrderAndOptimizeForClient)
    # 换算成min
    planWorkOrderAndOptimizeForClient_min = planWorkOrderAndOptimizeForClient / 60

    print("同步排程时间:%.2f min" % planWorkOrderAndOptimizeForClient_min)
