import pytest

from uiAutoTestHmtt import page
from uiAutoTestHmtt.page.page_in import PageIn
from uiAutoTestHmtt.tools.get_driver import GetDriver
from uiAutoTestHmtt.tools.get_log import GetLog
from uiAutoTestHmtt.tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    # 1.初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)

        # 2。通过统一入口类获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    # 2。结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

        """ 注意：不要调用self.driver.quit()方法，因为它没有置空操作 """

    # 3。登录测试业务方法
    # 运行命令：
    # (venv) guanhuajin@guanhuajindeMacBook-Pro HMPython %
    # pytest -v -s -m "mis_login" uiAutoTestHmtt/scripts/
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mis_login.yaml"))
    @pytest.mark.mis_login
    # def test_mis_login(self, username="testid", pwd="testpwd123", expect="管理员"):
    def test_mis_login(self, username, pwd, expect):
        # 1.调用登录业务方法
        self.mis.page_mis_login(username, pwd)

        # 2。调试断言信息
        print("获取的昵称为：", self.mis.page_get_nickname())
        try:
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis.base_get_img()
            # 抛异常
            raise

