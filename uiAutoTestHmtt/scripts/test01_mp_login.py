# coding=utf-8
import pytest

from uiAutoTestHmtt import page
from uiAutoTestHmtt.page.page_in import PageIn

from uiAutoTestHmtt.tools.get_driver import GetDriver
from uiAutoTestHmtt.tools.read_yaml import read_yaml


class TestMpLogin:
    # 初始化
    """
    类级别：参数化数据有多条时，一定使用类级别
    函数级别：参数化数据只有一条或没有时，两种级别都可以
    不知道参数化数据的情况下，使用类级别
    """
    print("hahahahh")
    def setup_class(self):
        print('hehhehheh')
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 通过统一入口类（PageIn）获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()


    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize('username,code,expect', read_yaml('mp_login.yaml'))
    @pytest.mark.test
    # def test_mp_login(self, username='13812345678', code='246810', expect='13812345678'):
    def test_mp_login(self, username, code, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username, code)
        # 断言
        print('\n 获取的昵称为：' + self.mp.page_get_nickname())

        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            # 输出错误日志
            print("错误原因：", e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise


"""
重点：
    断言的三种方式：
            相等：assert a == b 
            属于：assert h in hello
            布尔型： assert True/False
    断言必须进行捕获异常错误信息，断言出现异常要配合（日志、截图、抛异常一起使用）

    在线生成报告：allure server report
"""