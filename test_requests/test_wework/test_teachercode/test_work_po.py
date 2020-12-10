from test_requests.test_wework.GroupChat import GroupChat


class TestWework:
    secret = 'VReV5qJx-wdPh4ABEoPuB-yAYML1xoxsnCgDupQJ3zc'
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

    @classmethod
    def setup_class(cls):
        # 实例化对象
        # cls.token = WeWork().get_token(cls.secret)
        # 类对象
        # cls.token=WeWork.get_token(cls.secret)
        # setup-class和cls代表传入的第一参数是类
        cls.groupchat = GroupChat()

    def test_get_groupchat(self):
        r = self.groupchat.list()
        assert r['errcode'] == 0

    def test_get_groupchat_status(self):
        r = self.groupchat.list( status_filter=0)
        assert r['group_chat_list'][0]['status'] == 0

    def test_get_groupchat_detail(self):
        r = self.groupchat.list()
        chat_id = r['group_chat_list'][0]['chat_id']
        r1 = GroupChat().get(chat_id)
        assert r1['errcode'] == 0
        assert len(r1['group_chat']['member_list']) > 0
