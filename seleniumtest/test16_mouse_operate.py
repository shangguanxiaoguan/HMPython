from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 获取浏览器对象
driver = webdriver.Chrome()
driver.maximize_window()
# 打开URL
driver.get('https://www.baidu.com/')

# 实例化并获取ActionChains类
action = ActionChains(driver)

# 定位输入框，右击鼠标
input_a = driver.find_element_by_id("kw")
# action.context_click(input_a).perform()
sleep(2)

# # 移动到设置上，出现悬浮框 【鼠标悬停】
# setting = driver.find_element_by_id("s-usersetting-top")
# action.move_to_element(setting).perform()
# sleep(2)

# 输入搜索内容，并进行双击
input_a.send_keys("python")
action.double_click(input_a).perform()

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
