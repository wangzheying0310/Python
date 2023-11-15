import requests
import time

cookies = {
    'JSESSIONID': '5F9C25C05A3D4B1DA3D1DE8FBE907884',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IueOi-WWhuiOuSIsInVzZXJObyI6IldaWSIsImlhdCI6MTY5OTUyMDE1MSwiZXhwIjoxNjk5NTYzMzUxfQ.kJb3CFURmEb0HmYSUKrDhPg8z9eDZ-B95pZ63C8yfYU',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'GoClientId': 'oCdLMFvP8obZhjQHABxI',
    'GoUsrNo': 'WZY',
    'Origin': 'http://172.16.5.10',
    'Referer': 'http://172.16.5.10/scene',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'type': 'SupplyChainPlanner',
    'name': 'checkDMSceneState',
    'args': [],
    'userNo': 'WZY',
}
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

checkDMSceneState_start = time.perf_counter()

response_checkDMSceneState = requests.post(
    'http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
checkDMSceneState_end = time.perf_counter()

checkDMSceneState = checkDMSceneState_end - checkDMSceneState_start
# 打印时长
print("同步SCP基础数据时间:%.2f s" % checkDMSceneState)
# 换算成min
checkDMSceneState_min = checkDMSceneState / 60
# 打印min
print("同步SCP基础数据时间:%.2f min" % checkDMSceneState_min)
# 记录同步基础数据结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'type': 'SupplyChainPlanner',
    'name': 'synchronizeDigitalSupplyChainParameterForClient',
    'args': [],
    'userNo': 'WZY',
}
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

synchronizeDigitalSupplyChainParameterForClient_start = time.perf_counter()

response_synchronizeDigitalSupplyChainParameterForClient = requests.post(
    'http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
synchronizeDigitalSupplyChainParameterForClient_end = time.perf_counter()

synchronizeDigitalSupplyChainParameterForClient = synchronizeDigitalSupplyChainParameterForClient_end - synchronizeDigitalSupplyChainParameterForClient_start

# 打印时长
print("同步供应链参数时间:%.2f s" % synchronizeDigitalSupplyChainParameterForClient)
# 换算成min
synchronizeDigitalSupplyChainParameterForClient_min = synchronizeDigitalSupplyChainParameterForClient / 60
# 打印min
print("同步供应链参数时间:%.2f min" % synchronizeDigitalSupplyChainParameterForClient_min)
# 记录同步PP基础数据结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'type': 'SupplyChainPlanner',
    'name': 'synchronizeDigitalSupplyChainStructureForClient',
    'args': [],
    'userNo': 'WZY',
}

response = requests.post(
    'http://172.16.5.10/apim/v2/scene/supplychain-planner/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
)