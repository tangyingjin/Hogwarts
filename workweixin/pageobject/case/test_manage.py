from workweixin.pageobject.page.managepage import Manage


class TestManage:
    def setup(self):
        self.manage=Manage(reuse1=True)

    def testmanage(self):
        self.load_picture=self.manage.load_picture()
        assert '1581507855(1).jpg' in self.load_picture.get_picture()