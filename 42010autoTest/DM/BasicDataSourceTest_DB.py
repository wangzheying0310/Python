# -- coding:utf-8 --
import requests

# 基础数据来自DB


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
        # 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJOTyI6Ind6eSIsImlzcyI6IkdPT0RPIiwiSUQiOiIxMDEiLCJleHAiOjE3MDAxOTQzNTMsImlhdCI6MTcwMDAxNDM1MywianRpIjoiVVNFUl9UT0tFTi4xMDEifQ.YUYb7YCvtKdLmohXEV2xXe58gYgy19HpBOi-N0TSP40',
        'Client-Identity': '8ff1592731cb56dc10926a2b2229999c',
        # 'Content-Type': 'application/json',
    }
    response = requests.post('http://172.16.9.2:42010/api/auth/authentication/login', headers=headers, json=payload,
                             verify=False)
    # print(response.headers)
    print(response.status_code)
    # print(response.text)

    token = req.visit("post", url, json=payload, headers=headers, ).json()["data"]["token"]

    headers["Authorization"] = token

    print(token)

    print("修改")
    update_response = req.visit("post", "http://172.16.9.2:42010/api/engine/projects/2/table/data", json={
        'express': '系统参数\uffffModel03\uffff1',
        'codeVersionId': '143',
        'remark': '全部修改为DB',
        'operators': [
            {
                'tableName': 'KTBasicDataSource',
                'addRows': [],
                'updateRows': [
                    {
                        'tid': '1975992',
                        'row': {
                            'materialDictionarySource': 'DB',
                            'bomSource': 'DB',
                            'unitConversionSource': 'DB',
                            'productionVersionSource': 'DB',
                        },
                    },
                ],
                'deleteIds': [],
                'deleteAll': False,
            },
        ],
    }, headers=headers, verify=False).json()["data"]

    print(update_response)

    print("发送重启场景请求")

    restart_response = requests.put('http://172.16.9.2:42010/api/engine/2/scenes/restart/170', headers=headers,
                                    verify=False)

    print(restart_response)

    print("点击同步基础数据")

    synchronizeBasicData_response = req.visit("post", "http://172.16.9.2:42010/api/engine/2/scenes/170", json={
        'express': 'synchronizeBasicData()',
    }, headers=headers, verify=False).json()["data"]

    print("打开BOM")

    BOM_response = req.visit("post",
                             "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                             json={
                                 'express': 'this.billOfMaterials',
                             }, headers=headers).json()["data"]

    print("BOM数据个数：", BOM_response['count'])

    print("打开物料主数据")

    MaterialDictionary_response = req.visit("post",
                                            "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                            json={
                                                'express': 'this.materialDictionaries',
                                            }, headers=headers).json()["data"]

    print("物料主数据个数：", MaterialDictionary_response['count'])

    print("打开生产版本")

    ProductionVersion_response = req.visit("post",
                                           "http://172.16.9.2:42010/api/engine/2/scenes/170/read",
                                           json={
                                               'express': 'this.productionVersions',
                                           }, headers=headers).json()["data"]

    print("生产版本个数：", ProductionVersion_response['count'])

    print("计算BOM、物料主数据、生产版本个数")

    if BOM_response['count'] == MaterialDictionary_response['count'] == ProductionVersion_response['count'] == 0:
        print("未获取到数据，测试通过")
    else:
        print("测试未通过")




