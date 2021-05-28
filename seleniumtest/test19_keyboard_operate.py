from time import sleep

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# 获取浏览器对象
# driver = webdriver.Chrome()


driver = webdriver.Firefox()
driver.maximize_window()
# 打开URL
driver.get('https://www.baidu.com/')


# send_keys(Keys.BACKSPACE)  # 删除键
# send_keys(Keys.SPACE)  # 空格键
# send_keys(Keys.TAB)  # 制表键
# send_keys(Keys.ESCAPE)  # 回退键
# send_keys(Keys.ENTER)  # 回车键
# send_keys(Keys.CONTROL, 'a')  # 全选
# send_keys(Keys.CONTROL, 'c')  # 复制

input_a = driver.find_element_by_id("kw")
input_a.send_keys("python1")

# 删除1
input_a.send_keys(Keys.BACKSPACE)
# 全选
input_a.send_keys(Keys.CONTROL, 'a')

# 复制
input_a.send_keys(Keys.CONTROL, 'c')
# 粘贴
input_a.send_keys(Keys.CONTROL, 'v')


# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
