from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取浏览器对象
driver = webdriver.Firefox()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

driver.find_element(By.CSS_SELECTOR, "[placeholder='Email Address']").send_keys("123@qq.com")


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
