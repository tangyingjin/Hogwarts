import math

L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
# ⽤⼀⾏代码得出 [11, 1, 2, 3, 5]
var = list(set(L))
print(var)
# L = [1, 2, 3, 4, 5]，L[10:]的结果是？ 结果是输出空列表
# L = [1, 2, 3, 5, 6]，如何得出 '12356'？
l = [1, 2, 3, 5, 6]
l.pop(0)
print(l)

var = ''.join(["1", "2", '3', '4', '5'])
print(var)
var1 = [str(i) for i in l]
print(var1)
var2 = ''.join(var1)
print(var2)
a = 1
b = 1.0
c = 'w'
d = True
e = -1
print(f'{type(a)}\n', f'{type(b)}\n', f'{type(c)}\n', f'{type(d)}\n', f'{type(e)}\n')


# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$

def weather(F):
    c = (F - 32) / 1.8
    print('%.2f华氏温度=%.2f摄氏温度' % (F, c))


weather(690.9)


# 练习2：输入圆的半径计算计算周长和面积
def center(r):
    a = r * r * math.pi
    print('圆的面积是%.2f' % (a))


center(3)
# 字符串格式化
name = 'Bob'
gender = 'man'
print('我的名字是%s,是个%s' % (name, gender))
print('我的名字是%(name)s,是个%(gender)s' % {'name': '张三', 'gender': 'man'})
# 通过参数来以其他顺序引用变量
print(f'我的名字是{name},是个{gender}')
print(F'我的名字是{name},是个{gender}')
# 替换字段用大括号进行标记
print('我的名字是{},是个{}'.format(name, gender))
# 通过索引来以其他顺序引用变量
print('我的名字是{0},是个{1}'.format(name, gender))
print('我的名字是{1},是个{0}'.format(gender, name))
# 通过参数来以其他顺序引用变量
print('我的名字是{name1},是个{gender}'.format(name1=name, gender=gender))
# 从字典中读取数据使用**
data = {"name": "张三", "age": 18}
print('我的名字是{name},是个{age}'.format(**data))


# 输入年份判断是不是闰年


def fun():
    year = int(input("输入年份"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print(f"{year}是闰年")
    else:
        print("{year}不是闰年".format(year=year))
fun()

# fun()
#判断闰年，不是闰年，一直输入，直到输入闰年，退出
year=0
while (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        year=int(input("输入年份"))
        print(f"{year}是闰年")
        break


a,b=0,1
while b<10:
    print(b,end='')
    a,b=b,a+b

i=0
sum=0
while i<10:
    sum=sum+i
    i = i + 1
print(sum,i)