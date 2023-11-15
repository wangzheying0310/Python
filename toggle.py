# # coding=utf-8
# from playwright.sync_api import Playwright, sync_playwright, expect
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("www.baidu.com")
#     # page.goto("http://172.16.5.10/")
#     # page.get_by_placeholder("请输入用户名").click()
#     # page.get_by_placeholder("请输入用户名").fill("WZY")
#     # page.get_by_placeholder("请输入密码").click()
#     # page.get_by_placeholder("请输入密码").fill("123456")
#     # page.get_by_placeholder("请输入密码").press("Enter")
#     # page.get_by_placeholder("请选择场景").click()
#     # page.get_by_role("menuitem", name="模式3").click()
#     # page.get_by_role("listitem").filter(has_text="规则库").locator("i").nth(1).click()
#     # page.locator("div:nth-child(3) > div:nth-child(4)").first.click(button="right")
#     # page.locator("#b-menuitem-116").click()
#     # page.get_by_text("修改数据").click()
#     # page.get_by_text("14", exact=True).click()
#     # page.get_by_role("button", name="确定").click()
#     # page.locator(".el-tooltip").first.click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
import time
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IldhbmdaaGVZaW5nIiwidXNlck5vIjoiV1pZIiwiaWF0IjoxNjk5MzQ5MzI3LCJleHAiOjE2OTkzOTI1Mjd9.huE51gTXsSH1_rAbofuMRzN5NglDDWrGNY0VNNj9EUk',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'GoClientId': 'mZ1u7-DSetIzom8kAAGc',
    'GoUsrNo': 'WZY',
    'Origin': 'http://172.16.6.10',
    'Referer': 'http://172.16.6.10/user-mode',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'type': 'SupplyChainPlanner',
    'name': 'checkDMSceneState',
    'args': [],
    'userNo': 'WZY',
}

a = time.time()

response = requests.post(
    'http://172.16.6.10/apim/v2/scene/supplychain-planner/FX110/companion-method',
    headers=headers,
    json=json_data,
    verify=False,
)

b = time.time()

print(b - a)