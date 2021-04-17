import pytest

from uiAutoTestHmtt.page.page_in import PageIn
from uiAutoTestHmtt.tools.get_driver import GetDriver
from uiAutoTestHmtt.tools.get_log import GetLog
from uiAutoTestHmtt.tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppLogin:
    # 1.初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_app_driver()
        # 2。通过统一入口类获取PageAppLogin对象
        self.login = PageIn(driver).page_get_PageAppLogin()

    # 2。结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3。app登录测试业务方法
    @pytest.mark.parametrize("phone,code", read_yaml("test_app_login.yaml"))
    def test_app_login(self, phone, code):
        # 调用app登录业务方法
        self.login.page_app_login(phone, code)
        # 调试断言
        # print(self.login.page_is_login_success())
        try:
            assert self.login.page_is_login_success()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛出异常
            raise


