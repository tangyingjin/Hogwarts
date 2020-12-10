import requests


class GroupChat:
    token_url = ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'ww196cca1d41b2401c'
    corpsecret = 'VReV5qJx-wdPh4ABEoPuB-yAYML1xoxsnCgDupQJ3zc'

    def get_token(self):
        params = {"corpid": self.corpid, "corpsecret": self.corpsecret}
        r = requests.get(url=self.token_url,
                         params=params)
        self.token = r.json()['access_token']
        return self.token



        # todo:不同的应用有不同的secret，我们需要从外边传进来



        # todo:@classmethod
        #  def setup_class(cls):
        # 在pytest框架里跑用例，使用@classmethod类方法，必须使用setup_class这种格式；所有case运行前只运行一次