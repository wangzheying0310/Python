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

# DM生产版本数量与SCPM生产版本数量对比

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
    response = requests.post('http://172.16.5.10/apim/v2/auth/login', headers=headers, json=payload,
                             verify=False)
    print("访问状态码", response.status_code)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print("token", token)

    pro_version_response = req.visit("post",
                                     "http://172.16.5.10/apim/v2/scene/supplychain-planner/Model03/computeExprDatas",
                                     json={
                                         'ProductionVersion': {
                                             'condition': '',
                                             'sort': '',
                                             'computeExprs': {},
                                             '__page': {
                                                 'num': 1,
                                                 'size': 300,
                                             },
                                         },
                                     }, headers=headers).json()["data"]

    pro_version_dict = pro_version_response['ProductionVersion']

    pro_version_list = pro_version_dict['rows']

    print('供应链生产版本个数', pro_version_dict['total'])

    # print("供应链生产版本集合", pro_version_list)

    pro_version_dm_response =\
        req.visit("post",
                  "http://172.16.5.10/apim/v2/scene/dataManager/Model03/computeExprDatas",
                  json={
                      'ProductionVersionInDM': {
                          'condition': '',
                          'sort': '',
                          'computeExprs': {},
                          '__page': {
                              'num': 1,
                              'size': 300,
                          },
                      },
                  }, headers=headers).json()["data"]

    ProductionVersion_dict = pro_version_dm_response['ProductionVersionInDM']

    print('数据引擎生产版本个数', ProductionVersion_dict['total'])

    if ProductionVersion_dict['total'] == pro_version_dict['total']:
        print("个数一致，测试通过")
    else:
        print("测试未通过")



