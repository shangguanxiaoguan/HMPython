from time import sleep

from selenium import webdriver


"""
使用css查找页面元素
"""


# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
driver.get('http://numberwebsite2.tzwebsitetest.com/')

# 查找login并点击
driver.find_element_by_class_name('login').click()

sleep(1)

# 使用css id选择器定位 邮箱输入框   【前提：元素必须有id属性】
# driver.find_element_by_css_selector("#")   邮箱输入框没有id属性
driver.find_element_by_css_selector("[placeholder='Email Address']").send_keys("123@qq.com")

# 使用css 属性选择器定位密码输入框
driver.find_element_by_css_selector("[type='password']").send_keys("123456")

# 使用css class选择器   【前提：元素必须有class属性】
driver.find_element_by_css_selector(".el-button--default")
sleep(1)
# 找到关闭按钮，关闭登录弹框
driver.find_element_by_css_selector(".el-dialog__close").click()
sleep(1)

# 使用css 元素选择器
span = driver.find_element_by_css_selector("span").text
print("获取的span标签文本值：", span)

# 使用css 层级选择器
# driver.find_element_by_css_selector("div>div[class='tab-right-content']").click()

# 暂停3秒
sleep(2)

# 退出浏览器驱动
driver.quit()
