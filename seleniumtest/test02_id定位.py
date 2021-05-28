from time import sleep

from selenium import webdriver


# 获取浏览器对象
driver = webdriver.Firefox()
# 打开URL
driver.get('https://www.baidu.com/')

# 查找输入框
inputa = driver.find_element_by_id('kw')

# 输入内容
inputa.send_keys('python')

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()