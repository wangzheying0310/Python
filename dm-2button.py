from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    # 定义playwright运行在chromium浏览器
    # browser = playwright.chromium.launch(headless=False)
    # Google Chrome 和 Microsoft Edge浏览器都是用的 chromium 内核，所以只需加一个channel="chrome" 即可打开谷歌浏览器
    # 添加 channel="msedge" 即可打开Microsoft Edge浏览器
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    # 创建一个新的浏览器页面
    # 窗口最大化
    context = browser.new_context(no_viewport=True)
    # 创建一个新的标签页
    page = context.new_page()
    # 相当于在浏览器中输入了地址,然后回车
    page.goto("http://172.16.5.10/")
    # 按占位符定位输入
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("WZY")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("123456")
    # 通过显式和隐式可访问性属性进行定位
    # button通过名称为“登录”的角色定位元素
    page.get_by_role("button", name="登录").click()
    # 通过文本内容定位
    page.get_by_text("场景管理").click()
    # 不管元素存不存在，都会返回一个locator 对象，可以用到count() 方法统一元素的个数，如果元素个数是 0， 那么元素就不存在
    # page.locator("#sidebar_nav div").filter(has_text="场景管理").nth(2).click()
    # page.get_by_text("核料测试").click() #场景名称可修改
    # # page.get_by_text("模型场景类别场景组场景id场景名称创建人创建时间是否选择主场景自动激活存储方式处理状态 数据引擎 活动场景 StandardizedTesting 复现专用场景").click(button="right")
    # page.get_by_text("核料测试").click(button="right") #场景名称可修改
    # page.locator("div:nth-child(11) > div:nth-child(8) > .sceneCellStyle").click()
    # page.locator("#b-subgrid-36 div").filter(has_text="NuclearMaterial 核料测试 WZY 2023-03-15 10:03:51 内存").locator("i").first.click() #场景内容可修改
    # page.get_by_text("NuclearMaterial").click(button="right") #场景内容可修改
    # page.get_by_text("激活场景").click()
    # # page.locator("#b-subgrid-36 div").filter(has_text="performanceTesting 性能测试 WZY 2023-03-28 15:37:13 内存").locator("i").first.click()
    # page.get_by_placeholder("请选择场景").click()
    # page.get_by_role("menuitem", name="核料测试").click() #场景内容可修改
    # page.locator("#activate").first.click()
    # page.get_by_role("alert").click()
    # page.locator("#activate").nth(1).click()
    # page.get_by_role("alert").nth(1).click()
    # page.locator("#activate").nth(2).click()
    # page.get_by_role("alert").nth(1).click()
    # page.get_by_role("listitem", name="基础数据").get_by_text("基础数据").click()
    # page.locator("#el-popover-1663").get_by_text("SAP原始BOM").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
