'''
练习1：华氏温度转换为摄氏温度。
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。'''
F = float(input("请输入华氏温度:"))
C = (F - 32) / 1.8
print('%.1f华氏温度=%.1f摄氏温度' % (F, C))
# 占位符：%.1f float类型 %d int类型 %s 字符串类型
# 格式化输出：format用法:print('{1},{2}'.format('hello','world'))  print(f'{F:.1f}华氏温度={C:.1f}')

'''
练习2：输入圆的半径计算计算周长和面积
'''
import math
R = float(input('输入圆的半径:'))
C = 2 * math.pi * R
S = math.pi * R * R
print('圆的周长=%.2f,圆的面积=%.2f' % (C, S))

'''
练习3：输入年份判断是不是闰年。
输入年份 如果是闰年输出True 否则输出False
'''
year=int(input('输入年份：'))
is_leap=year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
# 比较运算符会产生布尔值，要不True,要不False.而逻辑运算符会对这些布尔值组合，最终也得到一个布尔值；比较运算符有的地方也称为关系运算符，包括==、!=、<、>、<=、>=；逻辑运算符：and or  not
list1 = ['1.a', '2.b', '3.c']
list2 = ['3.x', '1.y', '2.z']
list3=[j+':'+ i[2] for i in list1 for j in list2 if i[0] == j[0]]
for each in list3:
    print(each)

list1 = ['1.a', '2.b', '3.c']
for i in list1:
    print(i[0],i[1])
    print(type(i))
