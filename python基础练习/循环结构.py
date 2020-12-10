'''
练习1：用for循环实现1~100之间的偶数求和
'''
sum = 0
for i in range(1, 100, 2):
    sum += i
print('1-100之间的偶数之和为：', sum)
# (1,100)只能取到1和99，不包含100；取偶数是从2开始，我们可以写成（2,101,2）

sum = 0
for i in range(2, 101):
    if i % 2 == 0:
        sum += i
print('1-100之间的偶数之和为：', sum)

'''
练习2:计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
'''
import random

rand = random.randint(1, 100)
count = 0
while True:
    count += 1
    user = int(input('输入数字：'))
    if rand > user:
        print('大一点')
    elif rand < user:
        print('小一点')
    else:
        print('猜对了')
        break
print('一共猜了%d次' % count)

'''
练习3：输出乘法口诀表(九九表)
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

'''
练习4：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身因子的整数。
'''
import math
number = int(input('输入一个正整数：'))
seq=int(math.sqrt(number))
is_prime=True
for i in range(2,seq+1):
    if number % i ==0:
        is_prime=False
        break
# 先判断这个数被它的平方根是否能够整除，如果不能，就是true
if  is_prime is True and number !=1:
        print('%d是素数'%number)
else:
    print('%d不是素数' % number)
'''
练习5：输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
'''
number1=int(input('输入正整数：'))
number2=int(input('输入正整数：'))
if number1 > number2:
    number1,number2=number2,number1
for i in (number1,0,-1):
    if number1 % i ==0 and number2 % i==0:
        print('%d和%d的最大公约数是%d' % (number1, number2, i))
        print('%d和%d的最小公倍数是%d' % (number1, number2, number1 * number2 // i))
        break

'''
练习6：打印如下所示的三角形图案。
*
**
***
****
*****  
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
'''
for i in range(0,6):
    for j in range(i+1):
        print('*'*j)

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(0,row-i-1):
            print(' ',end='')
    for k in range(2*i+1):
            print('*',end='')
    print()

