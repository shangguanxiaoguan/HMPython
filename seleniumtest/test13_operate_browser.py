from time import sleep

from selenium import webdriver


# 1.获取浏览器驱动对象
driver = webdriver.Chrome()

# 2.打开url
driver.get("http://numberwebsite2.tzwebsitetest.com/")

sleep(2)

# 将浏览器最大化
driver.maximize_window()
# 暂停2秒
sleep(2)

# 设置固定大小 300,200  单位：像素
driver.set_window_size(300, 200)
# 暂停2秒
sleep(2)

# 移动浏览器窗口位置： X：320  Y：150
driver.set_window_position(x=320, y=150)
# 暂停2秒
sleep(2)

# 最大化
driver.maximize_window()

# 演示后退功能，必须先执行打开新的网站
driver.find_element_by_partial_link_text('FAQ').click()
# 暂停2秒
sleep(2)
# 执行后退
driver.back()

# 暂停2秒
sleep(2)
# 执行前进，前进必须放在后退操作之后
driver.forward()

sleep(2)
# 8. 关闭驱动对象
driver.quit()
