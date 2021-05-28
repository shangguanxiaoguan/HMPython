from time import sleep

from selenium import webdriver


# 1.获取浏览器驱动对象
driver = webdriver.Chrome()

# 最大化浏览器
driver.maximize_window()

# 2.打开url
driver.get("http://numberwebsite2.tzwebsitetest.com/")

sleep(2)

# 获取第一个输入框大小
input_size = driver.find_element_by_css_selector("input").size
print("第一个输入框大小为：", input_size)
# 获取页面上第一个超文本链接内容
text = driver.find_element_by_css_selector("a").text
print("第一个超文本链接内容为：", text)
# 获取页面上第一个超文本链接地址
att = driver.find_element_by_css_selector("a").get_attribute("href")
print("第一个超文本链接地址为：", att)
# 判断span元素是否可见
displayed = driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否可见：", displayed)
# 判断查询按钮是否可用
enabled = driver.find_element_by_css_selector("button").is_enabled()
print("查询按钮是否可用：", enabled)
# 判断复选框是否被选中
driver.find_element_by_xpath("//*[@type='button']/span").click()
print("点击完查询按钮")
selected = driver.find_element_by_xpath("//div[@class='checkbox-uncheck']").is_selected()
print("第一个价格复选框是否被选中：", selected)


sleep(2)

# 8. 关闭驱动对象
driver.quit()
