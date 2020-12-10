import json

import requests


class TestWework:
    corpid = 'ww196cca1d41b2401c'
    # secret = 'A5LUenGyWi8m5mxYwrkkfD2LtS7kJCZPkfYq3xpmh-4'
    secret = 'VReV5qJx-wdPh4ABEoPuB-yAYML1xoxsnCgDupQJ3zc'
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token = None

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={
                             "corpid": cls.corpid,
                             "corpsecret": cls.secret})
        assert r.json()['errcode'] == 0
        print(r.json())
        cls.token = r.json()['access_token']
    # setup-class和cls代表传入的第一参数是类

    def test_get_access_token_exist(self):
        assert self.token is not None

    groupchat_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'

    def test_get_groupchat(self):
        r = requests.post(url=self.groupchat_url,
                          params={
                              'access_token': self.token
                          },
                          json={
                              "offset": 0,
                              "limit": 100
                          }
                          )
        print(r.json())
        assert r.json()['errcode'] == 0
        print(r.headers['Content-Type'])
    # todo:此处为什么用json传，而不用data传，在实际工作中，如何判断一个接口该传入什么样的数据
    # 其实可以看请求头的 Content-Type字段 判断
    # 值: applocation／json                                为json格式
    # 值:application／x-www-from-urlencodeed               为data格式
    # 值:multipart/form-data                              为表单格式 用file传

    # todo:这个接口用json传，未指定headers中的content-type，默认为application/json


    groupchat_detail_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'

    def test_get_groupchat_detail(self):
        r = requests.post(url=self.groupchat_url,
                          params={
                              'access_token': self.token
                          },
                          json={
                              "offset": 0,
                              "limit": 100
                          }
                          )
        chat_id = r.json()['group_chat_list'][0]['chat_id']

        r = requests.post(url=self.groupchat_detail_url,
                          params={
                              "access_token": self.token
                          },
                          json={"chat_id": chat_id}
                          )
        print(json.dumps(r.json(),indent=2))
        assert r.json()['errcode'] == 0
        assert len(r.json()['group_chat']['member_list']) > 0
#封装的核心是把不变的东西封装起来，留下来变的
