from time import sleep

from selenium import webdriver


"""
注意：
     1. 只能定位 a 标签
     2. partial_link_text定位的元素内容支持模糊匹配
"""


# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

sleep(2)
# # 使用partial_link_text定位元素并点击
""" 注意：如果没有使用唯一代表词，默认操作符合条件的第一个元素 """
driver.find_element_by_partial_link_text('Contact').click()


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
