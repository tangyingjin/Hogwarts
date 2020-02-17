from workweixin.pageobject.page.mainpage import Main


class TestContact:
    def setup(self):
        self.main = Main(reuse1=True)

    def testaddmember(self):
        self.contact=self.main.goto_member().add_member(name='hi', acctid='hello', mobile='12345678903')
        assert self.contact.get_member()=='hi'


    def testupdatemember(self):
        self.main.goto_member().update_member()
