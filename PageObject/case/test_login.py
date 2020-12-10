from PageObject.page.index_page import Index
class TestLogin():
    def setup(self):
        self.index=Index()

    def test_login(self):
        register_page=self.index.goto_login().goto_register().register('bc')
        print("|".join(register_page.GetErrorMessage()))
        assert "请选择" in "|".join(register_page.GetErrorMessage())


