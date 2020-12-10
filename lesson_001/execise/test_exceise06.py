"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import os
import random


def print_directory_contents(sPath):
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


''''''

'''F:\新建文件夹\舟山社区测试相关'''

'''4.打乱一个排好序的list对象alist？shuffle() 方法将序列的所有元素随机排序。
5.现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
'''
alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
a = sorted(d.items(), key=lambda x: x[1])
for x in d.items():
    print(x[1])
print(a)
c = zip(d.keys(), d.values())
print()
d = sorted(c)
print(d)

'''7.请反转字符串 "aStr"?'''
str = 'aStr'
print(str[::-1])
'''8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}'''


def strtodict():
    str = 'k:1|k1:2|k2:3|k3:4'
    dict = {}
    for item in str.split('|'):
        print(item)
        key, value = item.split(':')
        print(key, value)
        dict[key] = value
    return dict


strtodict()

'''9.请按alist中元素的age由大到小排序'''
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
sorted(alist, key=lambda x: x['age'])

'''先按照成绩降序排序，相同成绩的按照名字升序排序'''
d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
      {'name': 'christ', 'score': 28}]
sorted(d1, key=lambda x: (-x['score'], x['name']))

list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])获取列表的切片
# print(list[10]) 会导致IndexError: list index out of range
# 输出[]空列表

'''11.写一个列表生成式，产生一个公差为11的等差数列'''
print([i * 11 for i in range(10)])

'''12.给定两个列表，怎么找出他们相同的元素和不同的元素？'''
list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list1)
set2 = set(list2)
# print(set1)
# print(set1&set2)
# print(set1^set2)

'''13.请写出一段python代码实现删除list里面的重复元素？'''


def toremove():
    lst = [1, 2, 3, 4, 3, 10, 2, 5, 1, 3, 5]
    for i in range(0, len(lst) - 1):
        if lst.count(lst[i]) >= 2:
            lst.remove(lst[i])
    return lst


# a = toremove()
print(a)
lst2 = [1, 2, 3, 4, 3, 10, 2, 5, 1, 3, 5]
print(list(set(lst2)))

'''列表转字典'''
lst = [1, 2, 3, 4]
lst1 = enumerate(lst)
