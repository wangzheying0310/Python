import time

import requests

cookies = {
    'JSESSIONID': 'D057B85EB5C3A731EC00B4FEDAB1F2C9',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IueOi-WWhuiOuSIsInVzZXJObyI6IldaWSIsImlhdCI6MTY5OTUxOTY4NSwiZXhwIjoxNjk5NTYyODg1fQ.M5Bye6ndPu1ZJNHJGpq-f83Vp6QNU4BibjAr66Ax274',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'JSESSIONID=D057B85EB5C3A731EC00B4FEDAB1F2C9',
    'GoClientId': 'T-x_1-y1qOoJFqdJABxA',
    'GoUsrNo': 'WZY',
    'Origin': 'http://172.16.5.10',
    'Referer': 'http://172.16.5.10/user-mode',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'type': 'DataManager',
    'name': 'synchronizeBasicDataForClient',
    'args': [],
    'userNo': 'WZY',
}
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

synchronizeBasicDataForClient_start = time.perf_counter()

response_synchronizeBasicDataForClient = requests.post(
    'http://172.16.5.10/apim/v2/scene/dataManager/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)

response = requests.post(
    'http://172.16.5.10/apim/v2/scene/dataManager/XingNeng1/computeExprDatas',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
synchronizeBasicDataForClient_end = time.perf_counter()

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
    'type': 'DataManager',
    'name': 'synchronizeBusinessDataForClient',
    'args': [],
    'userNo': 'WZY',
}
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

synchronizeBusinessDataForClient_start = time.perf_counter()

response_synchronizeBusinessDataForClient = requests.post(
    'http://172.16.5.10/apim/v2/scene/dataManager/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
synchronizeBusinessDataForClient_end = time.perf_counter()

synchronizeBusinessDataForClient = synchronizeBusinessDataForClient_end - synchronizeBusinessDataForClient_start
# 打印时长
print("同步业务数据时间:%.2f s" % synchronizeBusinessDataForClient)
# 换算成min
synchronizeBusinessDataForClient_min = synchronizeBusinessDataForClient / 60
# 打印min
print("同步业务数据时间:%.2f min" % synchronizeBusinessDataForClient_min)
# 记录同步业务数据结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

json_data = {
    'type': 'DataManager',
    'name': 'synchronizeSalesDataForClient',
    'args': [],
    'userNo': 'WZY',
}

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

synchronizeSalesDataForClient_start = time.perf_counter()

response_synchronizeSalesDataForClient = requests.post(
    'http://172.16.5.10/apim/v2/scene/dataManager/XingNeng1/companion-method',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
synchronizeSalesDataForClient_end = time.perf_counter()

synchronizeBusinessDataForClient = synchronizeSalesDataForClient_end - synchronizeSalesDataForClient_start
# 打印时长
print("同步销售数据时间:%.2f s" % synchronizeBusinessDataForClient)
# 换算成min
synchronizeBusinessDataForClient_min = synchronizeBusinessDataForClient / 60
# 打印min
print("同步销售数据时间:%.2f min" % synchronizeBusinessDataForClient_min)
# 记录同步业务数据结束系统时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))



