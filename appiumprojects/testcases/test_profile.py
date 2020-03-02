from appiumprojects.page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().start().main().goto_profile()

    def test_profile(self):
        assert '错误' in self.profile.login_by_password('152688828888', 'abcdefghj')
