from time import sleep

from selenium import webdriver


# 1.获取浏览器驱动对象
driver = webdriver.Chrome()

# 2.打开url
driver.get("http://numberwebsite2.tzwebsitetest.com/")

sleep(2)

# 3. 点击 Log in
driver.find_element_by_class_name("login").click()
sleep(2)

# 4.输入邮箱
driver.find_element_by_css_selector("[placeholder='Email Address']").send_keys("123@qq.com")
sleep(2)

# 5.输入密码
driver.find_element_by_css_selector("[placeholder='Password']").send_keys("123456")
sleep(2)

# 6. 重新输入邮箱 ——清空操作
driver.find_element_by_css_selector("[placeholder='Email Address']").clear()
driver.find_element_by_css_selector("[placeholder='Email Address']").send_keys("456@qq.com")
sleep(2)

# 7.点击登录按钮
driver.find_element_by_css_selector("button").click()
sleep(2)

# 8. 关闭驱动对象
driver.quit()
