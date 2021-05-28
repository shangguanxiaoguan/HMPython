from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


# 获取浏览器对象
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.maximize_window()
# 打开URL
driver.get('https://www.baidu.com/')

# 实例化并获取ActionChains类
action = ActionChains(driver)

# 定位输入框，python
input_a = driver.find_element_by_id("kw")
# 右击鼠标
action.context_click(input_a).perform()
# 发送p
input_a.send_keys("P")


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
