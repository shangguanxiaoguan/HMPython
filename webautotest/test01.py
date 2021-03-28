from time import sleep

from selenium import webdriver

# 获取浏览器驱动
driver = webdriver.Firefox()

# 打开URL
driver.get('http://www.baidu.com')

# 暂停3秒
sleep(3)

# 关闭浏览器驱动
driver.quit()
