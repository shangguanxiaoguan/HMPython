from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self, driver):
        """解决driver"""
        self.driver = driver

    # 查找 方法封装 loc一定是个列表或者元组
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30秒
        :param poll: 查找元素的频率 默认为0.5秒
        :return: 元素
        """
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))  # 匿名函数
        """
        参数解释：
            loc ：为元组或列表（*loc为解包==loc[0],loc[1]） 
            lambda x: x.find_element(*loc)  ： 匿名函数，x为driver
        
        """

    # 输入 方法封装
    def base_input(self, loc, value):
        """

        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 1。获取元素
        el = self.base_find(loc)

        # 2。清空操作
        el.clear()

        # 3。输入操作
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """

        :param loc: 元素定位信息
        """
        # 1。获取元素
        self.base_find(loc).click()
        # 2。点击按钮

    # 获取 元素文本
    def base_get_text(self, loc):
        """

        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        return self.base_find(loc).text


"""
base模块起名辅助：
    模块名编写：base.py
    类名编写：大驼峰方式将模块名抄进来，有下划线去掉下划线
    函数名编写：base+下划线+动词+[名词] （如base_input）
"""