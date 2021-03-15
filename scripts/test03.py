# coding=utf-8

"""
    1.多线程应用
    2。不同浏览器启动参数
"""
from selenium import webdriver

chrome = webdriver.DesiredCapabilities.CHROME.copy()
print(chrome)
# 修改默认平台名称
chrome['platform'] = 'MAC'
print(chrome)
