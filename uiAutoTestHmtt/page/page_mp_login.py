from uiAutoTestHmtt.base.base import Base


class PageMpLogin(Base):
    # 输入用户名
    def page_input_username(self):
        pass

    # 输入验证码
    def page_input_code(self):
        pass

    # 点击登录按钮
    def page_click_login_btn(self):
        pass

    # 获取昵称封装
    def page_get_nickname(self):
        pass

    # 组合业务方法（作用：把前面的步骤组合在一起，后面调用的时间就只用调用这一个方法）
    def page_mp_login(self):
        pass


"""
page模块起名辅助：
    模块名编写：
        page+下划线+模块名.py(如：page_login.py)
    
    类名编写：
        大驼峰方式将模块名抄进来，有下划线去掉下划线
    
    函数名编写：page+下划线+动词+下划线+名词 （page_input_username)

"""