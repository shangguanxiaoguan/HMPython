from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 1.获取浏览器驱动对象
driver = webdriver.Chrome()

# 将浏览器最大化
driver.maximize_window()

# 2.打开url
driver.get("http://numberwebsite2.tzwebsitetest.com/")
sleep(2)

# 刷新
# driver.find_element_by_css_selector("[placeholder='e.g.408']").send_keys("510")
elements = driver.find_elements(By.CSS_SELECTOR, "input")
elements[0].send_keys("510")
driver.find_element_by_partial_link_text("Home").click()
driver.refresh()

sleep(2)

# 获取title
title = driver.title
print("获取的页面title为：{}".format(title))

# 获取当前url
current_url = driver.current_url
print("获取的当前url为：", current_url)

# 关闭主窗口
driver.close()

# sleep(2)
# # 8. 关闭驱动对象
# driver.quit()
