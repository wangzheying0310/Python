import requests
import json


def send_dingtalk_message(webhook, message):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(webhook, headers=headers, data=json.dumps(data))
    return response.json()


# 在此处添加发送钉钉邮件的代码
webhook = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN"
message = "所有Python文件已执行完毕！"
send_dingtalk_message(webhook, message)
