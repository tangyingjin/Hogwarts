import requests


class WeWork:
    corpid = 'ww196cca1d41b2401c'
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token = dict()

    @classmethod
    def get_token(cls,secret):
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            cls_token=cls.get_access_token(secret)
            cls.token[secret] =cls_token['access_token']
        print(cls.token[secret])
        return cls.token[secret]

    @classmethod
    def get_access_token(cls,secret):
            r = requests.get(cls.token_url,
                             params={
                                 "corpid": cls.corpid,
                                 "corpsecret": secret})
            return r.json()
