from time import sleep

from selenium import webdriver


# 获取浏览器对象
driver = webdriver.Firefox()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

# 获取所有的input元素
elements = driver.find_elements_by_tag_name("input")
print(len(elements))
print("elements的类型：", type(elements))

# 输入内容
elements[0].send_keys("888")

# 通过遍历来输入
for el in elements:
    el.send_keys("408")

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
