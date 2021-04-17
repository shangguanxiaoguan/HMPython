import pytest

from uiAutoTestHmtt import page
from uiAutoTestHmtt.page.page_in import PageIn
from uiAutoTestHmtt.tools.get_driver import GetDriver
from uiAutoTestHmtt.tools.read_yaml import read_yaml


class TestMpArticle:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)

        # 2。获取统一入口类对象
        self.page_in = PageIn(driver)

        # 3。 获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()

        # 4。获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()


    # 2。结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3。测试发布文章方法
    @pytest.mark.parametrize("title, content, expect, channel", read_yaml("mp_article.yaml"))
    # def test_mp_article(self, title="test001-bj001", content="今晚炖火锅"):
    def test_mp_article(self, title, content, expect, channel):
        print("发布文章所属频道为：", channel)
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("发布文章结果为：", self.article.page_get_info())
