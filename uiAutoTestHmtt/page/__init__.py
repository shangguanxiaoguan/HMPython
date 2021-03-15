"""
这个文件的作用：可以直接通过包名.方法或者包名.变量的方式获取值
"""
from selenium.webdriver.common.by import By

"""以下数据为自媒体模块配置数据"""
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')  # .XXX css中的类选择器
# 昵称
mp_nickname = (By.CSS_SELECTOR, '.user-name')


"""
本小节总结：
    1。元素配置信息统一存放管理（__init__.py）
    2。能使用css选择器定位，不使用xpath定位
    3。css选择器中[属性名='属性值']为属性选择器，属性名无需添加@修饰。[.XXX]为class选择器，
P17看完
"""