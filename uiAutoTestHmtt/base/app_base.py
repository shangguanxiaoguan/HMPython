from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from uiAutoTestHmtt.base.base import Base
from uiAutoTestHmtt.tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):
    # 1. 查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        try:
            # 1.调用查找方法
            self.base_find(loc, timeout=3)
            log.info("在app页面中找到指定元素！")
            # 2. 输出信息
            print("找到：{}元素啦！".format(loc))
            # 3。返回True
            return True
        except:
            log.info("没有在app页面中找到指定元素")
            # 1. 输出信息
            print("未找到：{}元素！".format(loc))
            # 2。返回False
            return False

    # 2. 从右向左滑动屏幕
    def app_base_right_wipe_left(self, loc_area, click_text):
        log.info("正在调用 从右向左滑动方法")
        # 1. 查找区域元素
        el = self.base_find(loc_area)
        # 2。获取区域元素的位置 y坐标点
        y = el.location.get("y")
        # 3。获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4。 计算 start_x, start_y, end_x, end_y 【截图见语雀笔记中的app测试】
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5

        # 组合频道元素配置信息
        # loc = By.XPATH, "//*[contains(@text,'{}')]".format(click_text)

        # 在指定区域内查找指定元素——》加上父级元素【避免在文章中出现需要查找的元素字符】
        # loc = By.XPATH, "//*[@class='父级元素的class名称']//*[contains(@text,'{}')]".format(click_text)
        # 新写法：
        loc = By.XPATH, "//父级元素的class名称/*[contains(@text,'{}')]".format(click_text)
        # 5.循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2。捕获异常
            try:
                sleep(2)  # 为了解决模拟器慢的问题
                # 1. 查找元素
                el = self.base_find(loc, timeout=3)
                # 2。输出提示信息
                print("找到：{}元素啦！".format(loc))
                sleep(2)
                # 3。点击元素
                el.click()
                # 4。跳出循环
                break
            # 3。处理异常
            except:
                # 1。输出提示信息
                print("未找到：{}元素！".format(loc))
                # 2。滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4。判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1。输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 2。抛出未找到元素异常
                raise NoSuchElementException

    # 3. 从下向上滑动屏幕
    def app_base_down_wipe_up(self, loc_area, click_text):
        log.info("正在调用 从下向上滑动方法")
        # 1. 查找区域元素
        el = self.base_find(loc_area)
        # 2。获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4。 计算 start_x, start_y, end_x, end_y 【截图见语雀笔记中的app测试】
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 组合频道元素配置信息
        # loc = By.XPATH, "//*[contains(@text,'{}')]".format(click_text)

        # 在指定区域内查找指定元素——》加上父级元素【避免在文章中出现需要查找的元素字符】
        # loc = By.XPATH, "//*[@class='父级元素的class名称']//*[contains(@text,'{}')]".format(click_text)
        # 新写法：
        loc = By.XPATH, "//父级元素的class名称/*[contains(@text,'{}')]".format(click_text)
        # 5.循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2。捕获异常
            try:
                # 1. 查找元素
                el = self.base_find(loc, timeout=3)
                # 2。输出提示信息
                print("找到：{}元素啦！".format(loc))
                # 3。点击元素
                el.click()
                # 4。跳出循环
                break
            # 3。处理异常
            except:
                # 1。输出提示信息
                print("未找到：{}元素！".format(loc))
                # 2。滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4。判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1。输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 2。抛出未找到元素异常
                raise NoSuchElementException
