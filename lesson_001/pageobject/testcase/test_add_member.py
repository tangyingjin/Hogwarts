from lesson_001.pageobject.pages.mainpages import Main


class TestIndex:
    def test_add_member(self):
        main=Main(reuse=True)
        main.add_member().add_member()





