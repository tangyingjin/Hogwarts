l1 = [[1, 2], (30, 40)]
l2 = list(l1)

l1.append(100)

print(l1)
print(l2)

l1[0].append(3)

print(l1)
print(l2)

import copy

l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)

x = [1]
x.append(x)
y = copy.deepcopy(x)
print(x)


# x==y
# 运行报RecursionError: maximum recursion depth exceeded in comparison
# 是因为==操作符会递归地遍历对象的所有值，并逐一比较。而python为了防止栈崩溃，递归的层数是要限定的，不会无休止下去。
# todo:可变类型：可变类型（列表、字典、可变集合），名值存储在栈内存中
# todo:不可变类型：不可变类型（数字、字符串、元组、不可变集合），名存在栈内存中，值存在于堆内存中，但是栈内存会提供一个引用的地址指向堆内存中的值

def my_fun4(l2):
    l2 = l2 + [4]


l1 = [1, 2, 3]
my_fun4(l1)
print(l1)


def my_fun4(l2):
    l2 += [4]


l1 = [1, 2, 3]
my_fun4(l1)
print(l1)

# 下面的代码，l1,l2,l3是指同一个对象嘛？
l1=[1,2,3]
l2=[1,2,3]
l3=l2

print(id(l1))
print(id(l2))
print(id(l3))


# 下面的代码中，打印d最后的输出是什么？
# 可变对象引用
def func(d):
    d['a']=10
    d['b']=20
d={'a':1,"b":2}
func(d)
print(d)
# {'a':1,"b":2}
# 可变对象引用
def func(d):
    d.append(4)
d=[1,2,3]
print(id(d))
func(d)
print(d)
print(id(d))
# 还是同一个对象，id值一样

# 不可变对象引用
def func(d):
    d+'s'
d='adc'
func(d)
print(d)

# todo:若返回可变