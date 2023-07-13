from playwright.sync_api import Playwright, sync_playwright

# 第二种
playwright = sync_playwright().start()
# slow_mo 等待时间
browser = playwright.chromium.launch(headless=False,slow_mo=1000)
context = browser.new_context(viewport={'width':1920,'height':1080})
# 创建一个新的标签页
page = context.new_page()
page.goto('http://172.16.5.10:8000')
# 登录测试用例
page.fill('//*[@id="app"]/div/section/main/section/form/div[1]/div[1]/div/div[1]/div[1]/input','admin')
page.fill('//*[@id="app"]/div/section/main/section/form/div[2]/div[1]/div/div[1]/div[1]/input','123456')
page.click('//div[@class="n-form-item-blank"]/button/span')
# 上传文件
page.click('//div[@class="nav-bar"]/section[4]/article[2]')
page.click('//main[@class="platform-main"]/section/aside/section/ul[4]/li[2]')
# page.goto('http://172.16.5.10:8000/sys-plat-upgrade')

page.click('//div[@class="n-button n-button--default-type n-button--medium-type"]/span/i')

# page.click('//*[@id="app"]/div/section/main/section/section/div/section[1]/article[2]/div/div[3]/table/tbody/tr/td[8]/div/div/div[1]/span/i/i/svg')
page.click('//button[@class="n-button n-button--info-type n-button--medium-type n-button--color review-btn"]/span')
page.set_input_files(r'D:\Goodo\StandTesting\Product\platformVersion\2.1.3.2CM.zip')
page.click('//div[@class="modal-footer"]/button[1]/span')
browser.close