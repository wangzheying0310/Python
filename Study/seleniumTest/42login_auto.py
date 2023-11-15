from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
# 模拟键盘操作
from selenium.webdriver.common.keys import Keys
import time

service = Service()
# Chrome Options是一个配置chrome启动时属性的类
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=service, options=options)
# 设置浏览器大小：全屏
browser.maximize_window()
browser.get('http://172.16.9.2:42010/')
time.sleep(2)

username = browser.find_element(By.XPATH, '//input[@type="text"]')
username.send_keys('wzy')
password = browser.find_element(By.XPATH, '//input[@type="password"]')
password.send_keys('RSO@2019')
login_btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div/button')
login_btn.click()
# username.send_keys()
time.sleep(5)
# 设置后退
# browser.back()

# 设置前进
# browser.forward()

# 网页标题
print(browser.title)
# 当前网址
print(browser.current_url)
# 浏览器名称
print(browser.name)

# 网页源码
# print(browser.page_source)

# 设置分辨率 500*500
# browser.set_window_size(500,500)

# 关闭浏览器
# browser.close()