#!/usr/bin/python
# description      :基于微信的服务器API-通讯录管理-成员管理

import requests


class TestCreatUser:
    create_user_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
    access_token_url = ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    get_user_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
    corpid = 'ww196cca1d41b2401c'
    corpsecret = 'KcnP64SyLsaNoG3ibGTWLztmIIrRzk_qh34xCMDRYGI'

    @classmethod
    def setup_class(cls):
        payload = {"corpid": cls.corpid, 'corpsecret': cls.corpsecret}
        r = requests.get(url=cls.access_token_url, params=payload)
        print(r.json())
        assert r.json()['errcode'] == 0
        cls.token = r.json()['access_token']

    def test_create_user(self):
        params = {'access_token': self.token}
        data = {"userid": "zhangsan", "name": "张三", "department": [1, 2], "mobile": "13800000001"}
        r = requests.post(url=self.create_user_url, params=params, json=data)
        print(r.headers['Content-Type'])
        print(r.headers)
        assert r.json()['errmsg'] == 'created'
        # todo:为什么此处传data和json参数，打印的头部content-type信息是一样的

    # data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
    # data为str时，如果不指定content-type，默认为application/json
    # 不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
    # 用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式

    def test_get_user(self):
        payload = {"access_token": self.token, "userid": 'TangYingJin'}
        r = requests.get(url=self.get_user_url, params=payload)
        print(r.json())
        assert r.json()['errcode'] == 0

    update_user_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'

    def test_update_user(self):
        payload = {"userid": 'TangYingJin', 'name': '瑛瑾'}
        params = {'access_token': self.token}
        r = requests.post(url=self.update_user_url,
                          params=params,
                          json=payload)
        assert r.json()['errmsg'] == 'updated'

    '''将姓名汤瑛瑾修改成瑛瑾'''

    delete_user_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'

    def test_delete_user(self):
        params = {'access_token': self.token,
                  "userid": 'SanZhang'}
        r = requests.get(url=self.delete_user_url,
                         params=params)
        print(r.json())
        assert r.json()['errcode'] == 0

    batchdelete_user_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete'

    def test_batchdelete_user(self):
        params = {'accesss_token': self.token}
        payload = {
            "useridlist": ["hello", "123"]
        }
        r = requests.post(url=self.batchdelete_user_url,
                          params=params,
                          json=payload)
        print(r.json())
        assert r.json()['errcode'] == 0

    department_userlist = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'

    def test_department_userlist(self):
        params = {'access_token': self.token,
                  'department_id': 1,
                  'fetch_child': 1
                  }
        r = requests.get(url=self.department_userlist, params=params)
        print(r.json())

    department_userlist_detail = 'https://qyapi.weixin.qq.com/cgi-bin/user/list'
    userlist = []

    def test_department_userlist_detail(self):
        params = {'access_token': self.token,
                  'department_id': 1,
                  'fetch_child': 1}
        r = requests.get(url=self.department_userlist_detail, params=params)
        print(r.json()['userlist'][0]['name'])
        for i in r.json()['userlist']:
            self.userlist.append(i['name'])
        print(self.userlist)
