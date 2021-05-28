from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


# 获取浏览器对象
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.maximize_window()
# 打开URL
driver.get('https://www.baidu.com/')

# 实例化并获取ActionChains类
action = ActionChains(driver)

# 【视频里面的例子，红色块拖到绿色块后面】
# 获取源元素
source = driver.find_element_by_css_selector("#div1")
# 获取目标元素
target = driver.find_element_by_css_selector("#div2")
sleep(2)
action.drag_and_drop(source, target)

# 扩展  ===》通过坐标偏移量执行
# action.drag_and_drop_by_offset(source, xoffset=320, yoffset=180)

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
