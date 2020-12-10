# 经典python例子
# 1.说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
# 例如：$1^3 + 5^3+ 3^3=153$，从1-1000中寻找水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num //100 %10
    high = num //100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
# 2.实现将一个正整数反转，例如：将12345变成54321
num=int(input('从键盘上输入一个正整数'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
# 3.公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
# x 100块钱  y 鸡
