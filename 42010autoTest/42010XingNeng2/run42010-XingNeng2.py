import json
import requests
import time
from datetime import datetime

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJOTyI6Ind6eSIsImlzcyI6IkdPT0RPIiwiSUQiOiIxMDEiLCJleHAiOjE2OTk2MTAzMjUsImlhdCI6MTY5OTQzMDMyNSwianRpIjoiVVNFUl9UT0tFTi4xMDEifQ.hBqXmA89jInaPKb5qhIYOs7Y9-2oGYuEcUMDAPxFWuQ',
    'Client-Identity': '8ff1592731cb56dc10926a2b2229999c',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://172.16.9.2:42010',
    'Referer': 'http://172.16.9.2:42010/ruleBase',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'express': 'synchronizeBasicDataForClient()',
}

# 记录同步基础数据系统开始时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 记录同步基础数据开始时间
synchronizeBasicDataForClient_start = time.perf_counter()
# 发送请求
response_synchronizeBasicDataForClient = requests.post('http://172.16.9.2:42010/api/engine/4/scenes/41',
                                                       headers=headers, json=json_data)
# 记录同步基础数据结束时间
synchronizeBasicDataForClient_end = time.perf_counter()
# 计算总时长
synchronizeBasicDataForClient = synchronizeBasicDataForClient_end - synchronizeBasicDataForClient_start
# 打印时长
print("同步基础数据时间:%.2f s" % synchronizeBasicDataForClient)
# 换算成min
synchronizeBasicDataForClient_min = synchronizeBasicDataForClient / 60
# 打印min
print("同步基础数据时间:%.2f min" % synchronizeBasicDataForClient_min)
# 记录同步基础数据结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'express': 'synchronizeDigitalSupplyChainParameterForClient()',
}
# 记录同步供应链参数开始系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 记录同步供应链参数开始时间
synchronizeDigitalSupplyChainParameterForClient_start = time.perf_counter()
# 发送请求
response_synchronizeDigitalSupplyChainParameterForClient = requests.post(
    'http://172.16.9.2:42010/api/engine/4/scenes/41', headers=headers, json=json_data, verify=False)
# 记录同步供应链参数结束时间
synchronizeDigitalSupplyChainParameterForClient_end = time.perf_counter()
# 计算总时长
synchronizeDigitalSupplyChainParameterForClient = synchronizeDigitalSupplyChainParameterForClient_end - synchronizeDigitalSupplyChainParameterForClient_start
# 打印时长
print("同步供应链参数时间:%.2f s" % synchronizeDigitalSupplyChainParameterForClient)
# 换算成min
synchronizeDigitalSupplyChainParameterForClient_min = synchronizeDigitalSupplyChainParameterForClient / 60
# 打印min
print("同步供应链参数时间:%.2f min" % synchronizeDigitalSupplyChainParameterForClient_min)
# 记录同步供应链参数结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'express': 'synchronizeDigitalSupplyChainStructureForClient()',
}
# 记录同步数字供应链开始系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 记录同步数字供应链开始时间
synchronizeDigitalSupplyChainStructureForClient_start = time.perf_counter()
# 开启调用分析
response_analyse_start = requests.post('http://172.16.9.2:42010/api/engine/call/4/41/analyse/start', headers=headers,
                                       verify=False)
# 发送请求
response_synchronizeDigitalSupplyChainStructureForClient = requests.post(
    'http://172.16.9.2:42010/api/engine/4/scenes/41', headers=headers, json=json_data)
# 记录同步数字供应链结束时间
synchronizeDigitalSupplyChainStructureForClient_end = time.perf_counter()
# 计算总时长
synchronizeDigitalSupplyChainStructureForClient = synchronizeDigitalSupplyChainStructureForClient_end - synchronizeDigitalSupplyChainStructureForClient_start
# 打印时长
print("同步数字供应链时间:%.2f s" % synchronizeDigitalSupplyChainStructureForClient)
# 换算成min
synchronizeDigitalSupplyChainStructureForClient_min = synchronizeDigitalSupplyChainStructureForClient / 60
# 记录同步数字供应链结束时间
print("同步数字供应链时间:%.2f min" % synchronizeDigitalSupplyChainStructureForClient_min)
# 按时间格式保存文件
with open(f"./data-{datetime.now().strftime('%Y,%m,%d %H-%M-%S')}.json",'w') as f:
# 获取请求结果
    response_analyse_result = requests.get('http://172.16.9.2:42010/api/engine/call/4/41/analyse/result',
                                           headers=headers, verify=False)
    print(response_analyse_result.json()["data"])
    json.dump(response_analyse_result.json(), f, ensure_ascii=False)
# 结束分析
response_analyse_end = requests.post('http://172.16.9.2:42010/api/engine/call/4/41/analyse/end', headers=headers,
                                     verify=False)
# 记录同步数字供应链结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'express': 'synchronizeSalesDataForClient()',
}

# 记录同步销售需求开始系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 记录同步销售需求开始时间
synchronizeSalesDataForClient_start = time.perf_counter()
# 发送请求
synchronizeSalesDataForClient_response = requests.post('http://172.16.9.2:42010/api/engine/4/scenes/41',
                                                       headers=headers, json=json_data)
# 记录销售需求结束时间
synchronizeSalesDataForClient_end = time.perf_counter()
# 计算总时长
synchronizeSalesDataForClient = synchronizeSalesDataForClient_end - synchronizeSalesDataForClient_start
# 打印时长
print("同步销售需求时间:%.2f s" % synchronizeSalesDataForClient)
# 换算成min
synchronizeSalesDataForClient_min = synchronizeSalesDataForClient / 60

print("同步销售需求时间:%.2f min" % synchronizeSalesDataForClient_min)
# 记录同步销售需求结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'express': 'algorithm.capacityPlanningAlgorithm()',
}
# 记录优化开始系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 记录优化开始时间
capacityPlanningAlgorithm_start = time.perf_counter()
# 发送请求
capacityPlanningAlgorithm_response = requests.post('http://172.16.9.2:42010/api/engine/4/scenes/41', headers=headers,
                                                   json=json_data)
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
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
