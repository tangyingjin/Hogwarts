'''微信接口-客户群管理'''

from test_requests.test_wework.test_groupcontact.api.groupchat_po import GroupChat_PO

class TestGroupChat:

    grouplist = GroupChat_PO()

    def test_grouplist(self):
        r = self.grouplist.grouplist()
        assert r['errcode'] == 0

    def test_grouplist_status(self):
        r = self.grouplist.grouplist(status_filter=0)
        assert r['errcode'] == 0
    # todo:获取客户详情的用例和获取客户群列表的用例最好不要耦合，要独立

    def test_grouplist_detail_url(self):
        r = self.grouplist.grouplist()
        chat_id = r['group_chat_list'][0]['chat_id']
        r1 = self.grouplist.grouplist_detail(chat_id)
        assert len(r1['group_chat']['member_list']) > 1

#     todo:入参决定了测试数据，返回值决定了断言的数据
