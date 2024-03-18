# -- coding:utf-8 --

import requests


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
# 获取到 PISPIP 中的所有数据
PISPIP_response = \
    req.visit("post",
              "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/computeExprDatas",
              json={
                  'ProductInStockingPointInPeriod': {
                      'condition': '',
                      'sort': '',
                      'computeExprs': {},
                      '__page': {
                          'num': 1,
                          'size': 3000,
                      },
                  },
              }, headers=headers).json()["data"]

ProductInStockingPointInPeriod_dict = PISPIP_response['ProductInStockingPointInPeriod']

# 获取PISPIP类中的productId（产品代码）、allFulfilledDemandQuantityForOG（满足量）、originalSalesDemandQuantity（需求量）、start（开始时间）、end（结束时间）、resourceReason（设备原因）、materialReason 物料原因、unfulfilledReason（不满足原因）
filtered_data = [
    {
        'productId': row['productId'],
        'allFulfilledDemandQuantityForOG': row['allFulfilledDemandQuantityForOG'],
        'originalSalesDemandQuantity': row['originalSalesDemandQuantity'],
        'start': row['start'],
        'end': row['start'],
        'resourceReason': row['resourceReason'],
        'materialReason': row['materialReason'],
        'unfulfilledReason': row['unfulfilledReason']
    }
    # 过滤掉originalSalesDemandQuantity 需求量不等于 0 的
    for row in ProductInStockingPointInPeriod_dict['rows']
    if row['originalSalesDemandQuantity'] != 0
]

print("获取所有产品的需求、满足量", filtered_data)

unfulfilled_product = []
fulfilled_product = []
for item in filtered_data:
    # 将同产品同周期的需求量与满足量进行对比，若不相等则存入不满足需求产品
    if item['allFulfilledDemandQuantityForOG'] != item['originalSalesDemandQuantity']:
        # print('需求不满足产品', item['productId'], item['unfulfilledReason'])
        unfulfilled_product.append((item['productId'], item['unfulfilledReason']))
    # 若相等则存入满足需求产品
    else:
        # print('需求满足产品', item['productId'])
        fulfilled_product.append(item['productId'])
print("需求不满足的产品、原因", unfulfilled_product)
print("需求满足的产品", fulfilled_product)

for item in unfulfilled_product:
    if item[1] == '':
        print('没有需求不满足原因提示的产品代码', item[0])
#         print('存在有没提示的需求，测试不通过')

# # 遍历列表
# for item in unfulfilled_product:
#     # 判断值中是否包含'库存过低'
#     if '库存过低' in item[1]:
#         # 打印键和值
#         print(f'键： {item[0]}, 值： {item[1]}')


for item in unfulfilled_product:
    key, value = item
    if "库存过低" in value:
        print(f"键：{key}")
        print(f"值：{value}")
        start = value.find(":") + 1
        end = value.find("-")
        print(f":到-中间的数据：{value[start:end]}")
