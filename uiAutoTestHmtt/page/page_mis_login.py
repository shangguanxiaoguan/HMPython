from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.web_base import WebBase
from uiAutoTestHmtt.tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):
    # 1. 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 2。输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 3。点击登录按钮
    def page_click_login_btn(self):
        # 1.处理js（因为登录按钮不可点击，要先处理成可点击的）
        js = "document.getElementById('inp1').disabled=false"
        # 执行js
        self.driver.execute_script(js)
        # 2。点击登录按钮
        self.base_click(page.mis_login_btn)

    # 4。获取昵称封装
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 5。组合后台管理登录业务方法
    def page_mis_login(self, username, pwd):
        log.info("正在调用后台管理系统登录业务方法，用户名：{}  密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 6。组合后台管理成功登录依赖方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用后台管理系统成功登录依赖方法，用户名：{}  密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
