from pprint import pprint

import requests
from requests import Response


def test_requests():
    r = requests.get('https://home.testing-studio.com/categories.json')
    print(r.json())
    print(r.status_code)
    pprint(r)
    assert r.status_code == 200


# todo:print()和pprint()都是python的打印模块，功能基本一样;唯一的区别就是pprint()模块打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果。特别是对于特别长的数据打印，print()输出结果都在一行，不方便查看，而pprint()采用分行打印输出，所以对于数据结构比较复杂、数据长度较长的数据，适合采用pprint()打印方式


def test_get():
    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         'b': 2,
                         'c': 'ccccc'
                     })
    print(r.json())
    assert r.status_code == 200


# todo:get的请求参数放在params里，params=payload;payload={"key1":"value1","key2":"value2"}

def test_post():
    r = requests.post("http://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          'b': 2,
                          'c': 'ccccc'
                      },
                      data={
                          "a": 11,
                          'b': 21,
                          'c': 'cccccc'})

    assert r.status_code == 200

    print(r.json())


# todo:post的Form请求构造参数放在data里，data=payload;payload={"key1":"value1","key2":"value2"}
# {'args': {}, 'data': '', 'files': {}, 'form': {'a': '1', 'b': '2', 'c': 'ccccc'}}

def test_upload():
    # url="http://httpbin.org/post"
    proxies={
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    r = requests.post(url = "http://httpbin.testing-studio.com/post",
                      files={"file": open('../../__init__.py', 'rb')},
                      proxies=proxies
                      )
    print(r.json())


def test_post1():
    r = requests.post("http://httpbin.testing-studio.com/post",
                      data={
                          "a": 11,
                          'b': 21,
                          'c': 'cccccc'},
                      headers={
                          "h": "test-demo"
                      })
    print(r.json())
    assert r.json()['headers']['H'] == 'test-demo'


def test_proxy():
    proxies={
        'http':'http://127.0.0.1:8888',
        'https':'http://127.0.0.1:8888'
    }
    r=requests.post(url="http://httpbin.org/post",
                    data={
                        "a":1,
                        "b":2,
                        "c":3
                    },
                    proxies=proxies,
                    verify=False)
                    # 关闭验证
    print(r.json())
    assert r.status_code==200

# session机制
# https校验：加verify=False
# hook机制：
# 请求体封装
# 请求体定义：request封装
# ❖ 响应结果重定义：hook机制
# ❖ 场景：⾃动加解密、通⽤⽇志、通⽤处理

def test_get_hook():
    def modfiy_response(r:Response,*args,**kargs):
        r.hock="Modify CUSESS"
        return r
    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         'b': 2,
                         'c': 'ccccc'
                     },
                     hooks={'response':[modfiy_response]})
    print(r.json())
    print(r.hock)
    assert r.status_code == 200