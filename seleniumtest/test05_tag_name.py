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
""" 注意：页面中如果存在多个相同的标签名，默认返回第一个标签元素 """
driver.find_element_by_tag_name('input').send_keys('1234@qq.com')


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
