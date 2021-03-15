# coding=utf-8

"""
    目标：Selenium Grid的使用
    需求：
        1。使用Chrome浏览器
        2。打开百度并搜索python关键字
        3。暂停3秒，关闭浏览器

"""


# 导包
import time
from selenium import webdriver


# 获取driver
#driver = webdriver.Chrome()


"""
重点 driver 获取
"""
cap = {
    "browserName": "chrome",
    "version": "",
    "platform": "MAC"
}
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)

# 打开百度
driver.get('http://www.baidu.com')

# 输入关键字
driver.find_element_by_id("kw").send_keys('python')

# 点击搜索按钮
driver.find_element_by_id('su').click()

# 暂停3秒 关闭浏览器
time.sleep(3)
driver.quit()

"""
总结：
   1。易错：
     1.1 browserName单词拼写
     1.2 浏览器及驱动不兼容
   2。注意：
     2.1 hub及node节点已正确启动
     2.2 连接hub中央节点地址可以从hub节点启动窗口复制，IP地址只要能访问hub节点机器即可

"""