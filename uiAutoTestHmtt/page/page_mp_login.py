from time import sleep

from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.base import Base, log

# class PageMpLogin(Base):
from uiAutoTestHmtt.base.web_base import WebBase


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)

    # 获取昵称封装  ---> 测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法（作用：把前面的步骤组合在一起，后面调用的时间就只用调用这一个方法）
    # ---->测试脚本层调用
    def page_mp_login(self, username, code):
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
        # self.page_get_nickname()

    # 组合业务方法 -》发布文章依赖使用
    def page_mp_login_success(self, username="13812345678", code="246810"):
        log.info("正在调用自媒体登录业务方法=====")
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()


"""
page模块起名辅助：
    模块名编写：
        page+下划线+模块名.py(如：page_login.py)

    类名编写：
        大驼峰方式将模块名抄进来，有下划线去掉下划线

    函数名编写：page+下划线+动词+下划线+名词 （page_input_username)

"""