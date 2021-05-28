from time import sleep

from selenium import webdriver


# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

# 找到Log in按钮并点击
driver.find_element_by_class_name('login').click()

sleep(1)

# # 查找邮箱输入框并输入内容
# driver.find_element_by_class_name('material-input-inner email-input fc-000 margin-bottom-2').send_keys('adfd@qq.com')
#
# # 查找密码输入框并输入内容
# driver.find_element_by_class_name('material-input-inner email-input fc-000 margin-bottom-2').send_keys('123456')

# # 输入内容
# inputa.send_keys('python')

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
