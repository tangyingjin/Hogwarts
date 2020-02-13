from workweixin.pageobject.page.mainpage import Main


class TestAddMember:
    def setup(self):
        self.main = Main(reuse=True)

    def testaddmember(self):
        self.main.goto_member().add_member(name='hi', acctid='hello', mobile='12345678903')

    def testupdatemember(self):
        self.main.goto_member().update_member()
