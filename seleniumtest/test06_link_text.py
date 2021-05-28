from time import sleep

from selenium import webdriver


"""
注意：
     1. 只能定位 a 标签
     2. link_text定位的元素内容必须为全部匹配
"""


# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

sleep(2)
# # 使用link_text定位元素并点击
""" 注意：页面中如果存在多个相同的标签名，默认返回第一个标签元素 """
driver.find_element_by_link_text('Contact Us').click()


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
