# coding=utf-8
"""
  需求：
     1。使用百度搜索python案例
     2。分别在Chrome和Firefox中运行

"""
import threading
from time import sleep
                                  

# 封装 获取百度
from selenium import webdriver


def get_baidu(driver):
    # 获取URL
    driver.get('http://www.baidu.com')
    # 输入搜索关键词
    driver.find_element_by_id('kw').send_keys('python')
    # 点击搜索按钮
    driver.find_element_by_id('su').click()
    # 暂停3秒，关闭浏览器
    sleep(3)
    driver.quit()


# 封装 driver
def get_driver(browser):
    # 定义空变量
    cap = None
    # 判断浏览器类型
    if browser == 'chrome':
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == 'firefox':
        cap = webdriver.DesiredCapabilities.FIREFOX.copy()
    # 修改默认平台名称
    cap['platform'] = 'MAC'
    # 返回driver
    return webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)


# 遍历多线程
# 定义浏览器列表
browser_name = ['chrome', 'firefox']
for browser in browser_name:
    driver = get_driver(browser)
    threading.Thread(target=get_baidu, args=(driver,)).start()   # 注意args传参的写法

