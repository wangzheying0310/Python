# -- coding:utf-8 --
# 测试生成周期长度是否正确
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

    print("修改周期")

    response = \
        req.visit("post",
                  "http://172.16.5.10/apim/v2/branch/model/supplychain-planner/%E5%9C%BA%E6%99%AF%E5%8F%82%E6%95%B0:XingNeng:4/add-kts",
                  json={
                      'createUser': 'WZY',
                      'branchName': 'XingNeng',
                      'remark': '保存',
                      'vos': [
                          {
                              'ktIdentity': 'com.aps.model.scpm.KTPeriodDefinition',
                              'deleteAll': False,
                              'deleteIds': [],
                              'addRows': [],
                              'updateRows': [
                                  {
                                      'ktid': 1,
                                      'id': '1',
                                      'length': 6,
                                      'minLength': 0,
                                      'sequenceNr': 2,
                                      'timeUnit': 'Week',
                                  },
                              ],
                          },
                      ],
                  }, headers=headers).json()["data"]
    print(response)

    print("同步基础数据开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeBasicDataForClient_start = time.perf_counter()

    response_synchronizeBasicDataForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng/companion-method", json={
            "type": "SupplyChainPlanner",
            "name": "synchronizeBasicDataForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers).json()["data"]

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
        req.visit("post", "http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng/companion-method", json={
            "type": "SupplyChainPlanner",
            "name": "synchronizeDigitalSupplyChainParameterForClient",
            "args": [],
            "userNo": "WZY"
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

    print("同步数字供应链开始系统时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    synchronizeDigitalSupplyChainStructureForClient_start = time.perf_counter()

    response_synchronizeDigitalSupplyChainStructureForClient = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng/companion-method", json={
            "type": "SupplyChainPlanner",
            "name": "synchronizeDigitalSupplyChainStructureForClient",
            "args": [],
            "userNo": "WZY"
        }, headers=headers, verify=False).json()["data"]

    synchronizeDigitalSupplyChainStructureForClient_end = time.perf_counter()
    # 计算总时长
    synchronizeDigitalSupplyChainStructureForClient = synchronizeDigitalSupplyChainStructureForClient_end - synchronizeDigitalSupplyChainStructureForClient_start

    # 打印时长
    print("同步数字供应链时间:%.2f s" % synchronizeDigitalSupplyChainStructureForClient)
    # 换算成min
    synchronizeDigitalSupplyChainStructureForClient_min = synchronizeDigitalSupplyChainStructureForClient / 60
    # 记录同步数字供应链结束时间
    print("同步数字供应链时间:%.2f min" % synchronizeDigitalSupplyChainStructureForClient_min)

    response_look_period = \
        req.visit("post", "http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng/value-set", json={
            'UnitPeriod': [
                {
                    'key': 'startDate',
                    'condition': '',
                },
            ],
        }, headers=headers, verify=False).json()["data"]
    print(response_look_period)

    # 提取'UnitPeriod'对应的字典
    unit_period_dict = response_look_period['UnitPeriod']

    # 获取'startDate'对应的列表
    start_date_list = unit_period_dict['startDate']

    # 计算列表的长度
    count = len(start_date_list)

    print("当前生成的周期数为", count)
