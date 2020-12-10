import requests
class BasePage:
    corpid = 'ww196cca1d41b2401c'
    corpsecret = 'KcnP64SyLsaNoG3ibGTWLztmIIrRzk_qh34xCMDRYGI'
    access_token_url = ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'

    @classmethod
    def get_token(cls):
        params={'corpid':cls.corpid,
                'corpsecret':cls.corpsecret}
        r=requests.get(cls.access_token_url,params=params)
        cls.token=r.json()['access_token']
        return cls.token