from time import sleep

from selenium import webdriver


"""
使用Xpath查找页面元素
"""


# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

# 查找login并点击
driver.find_element_by_class_name('login').click()

sleep(1)

# 使用绝对路径定位 邮箱输入框
# driver.find_element_by_xpath('/html/body/div/input/')  # 绝对路径使用失败
driver.find_element_by_xpath('//input[@placeholder="Email Address"]').send_keys('123@qq.com')

# 使用相对路径定位密码输入框
# driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('123456')


# 使用路径结合属性
driver.find_element_by_xpath('//input[@placeholder="Password" and @type="password"]').send_keys('123456')

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
