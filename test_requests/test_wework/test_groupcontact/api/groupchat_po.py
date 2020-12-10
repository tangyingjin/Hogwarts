import json
import requests
from test_requests.test_wework.test_groupcontact.api.GroupChat import GroupChat

class GroupChat_PO:
    grouplist_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'

    token = GroupChat().get_token()

    def grouplist(self,offset=0,limit=100,**kwargs):
        # todo:善用位置参数，**kwargs
        params = {"access_token": self.token}
        payload = {"offset": offset,
                   "limit": limit}
        print(payload)
        print(kwargs)
        payload.update(kwargs)
        print(payload)
        r = requests.post(url=self.grouplist_url,
                          params=params,
                          json=payload)
        print(json.dumps(r.json(),indent=2))
        return r.json()

    def grouplist_detail(self,chat_id):
        grouplist_detail_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        params = {"access_token":self.token}
        json = {"chat_id": chat_id}
        r1 = requests.post(url=grouplist_detail_url,
                           params=params,
                           json=json)
        return r1.json()