# encoding=utf-8
'''
练习1：英制单位英寸与公制单位厘米互换
'''
s = float(input('输入长度：'))
unit = input('请输入单位：')
if unit == '英寸' or unit == 'in':
    print('%.2f英寸 = %.2f厘米' % (s, s * 2.54))
elif unit == '厘米' or unit == 'cm':
    print('%.2f英寸 = %.2f厘米' % (s, s / 2.54))
else:
    print("请输入有效单位：")

'''
练习2：百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
'''
score = float(input('请输入分数：'))
if score >= 90:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 80:
    print('D')
else:
    print('E')
# 老师答案：
score = float(input('请输入分数：'))
if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 80:
    grade = 'D'
else:
    grade = 'E'
print('该学生的等级是%s' % grade)

'''
练习3：输入三条边长，如果能构成三角形就计算周长和面积。
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
'''
import math
a=float(input('输入边长 a:'))
b=float(input('输入边长 b:'))
c=float(input('输入边长 c:'))
if a + b > c and a + c > b and b + c > a:
    C=a+b+c
    p=C/2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('三角形的周长为%.2f,面积为%.2f' %(C,S))
else:
    print('不能构成三角形')