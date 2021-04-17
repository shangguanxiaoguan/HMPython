from time import sleep

from selenium import webdriver

# 导包
import appium.webdriver

from uiAutoTestHmtt import page


class GetDriver:
    # 1. 声明变量
    """ 为了方便通过类名.变量的形式调用到该变量，所以声明成私有变量

        目的是为了方便调用，不用实例化
     """
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2。获取driver方法
    """ 为了方便类名.函数名的形式调用到该方法，所以声明成类方法 """

    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空

        """
        driver为类属性，设置之前必须进行判断是否为空：

        目的：保证多次调用获取方法，返回同一个对象


        """

        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            sleep(2)
            print("------" + str(cls.__web_driver))
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)

        # 返回driver
        return cls.__web_driver

    # 3。退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            """ 
              重点：关闭driver必须置空操作
                 原因：1。driver执行quit方法后对象地址保留，不为空
                      2。避免下条用例调用获取driver能正常获取对象，必须置空

             """
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断 __app_driver 为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填，只要不为空即可
            desired_caps['deviceName'] = 'hkhkfd-jfkdsfn-jdfh'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None


if __name__ == '__main__':
    # 需要启动Appium服务
    GetDriver.get_app_driver()
    sleep(1)
    GetDriver.quit_app_driver()

