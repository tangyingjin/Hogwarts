from selenium import webdriver


class PageBase:
    def __init__(self):
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(4)
            self.driver.get('https://work.weixin.qq.com')

'''从index_page.py和register_page.py方法中，抽取出_init_方法，运行不成功
是因为：test_index.py中，初始化了Index实例，Index继承了PageBase类，初始化了_init_方法，打开了企业微信首页；再执行了goto_register方法后
再register的PO，该PO也继承了PageBase类，导致再次打开了企业微信首页，再继续执行输入名称报异常
所以需要分两步，见basepages.py'''



