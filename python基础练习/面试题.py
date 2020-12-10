# 1.一行代码实现1--100之和
print(sum(range(100)))

# 2.如何在一个函数内部修改全局变量
i = 1


def func():
    global i
    i=2
    print(i)


func()
print(i)


# 3.列出5个python标准库 time re
# 4.字典如何删除键和合并两个字典
d={'a':1,"b":2}
del d['a']
print(d)

d={'a':1,"b":2}
e={'c':1,"d":2}

d.update(e)
print(d)

# 谈下python的GIL
