from time import sleep


from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.app_base import AppBase
from uiAutoTestHmtt.tools.get_log import GetLog
from uiAutoTestHmtt.tools.read_yaml import read_yaml

log = GetLog.get_logger()


class PageAppLogin(AppBase):
    # 1. 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 2。输入验证码
    def page_input_code(self, code):
        self.base_input(page.app_code, code)

    # 3。点击登录按钮
    def page_click_login_btn(self):
        # 建议等待1-2秒
        sleep(2)
        self.base_click(page.app_login)

    # 4。判断页面是否存在 我的菜单
    def page_is_login_success(self):
        return self.app_base_is_exist(page.app_me)

    # 5。组合登录业务方法
    def page_app_login(self, phone, code):
        log.info("正在调用app登录业务方法")
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()
        # self.page_is_login_success()

    # 6。组合登录依赖成功业务方法
    def page_app_login_success(self, phone="13812345678", code="246810"):
        log.info("正在调用app登录业务方法")
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()
