'''
# 打印左下角三角形：for i in range(10):之后，range(0,i)
# 打印右上角三角形：在左下角的基础上，将"－"变成" "空格
'''
row=int(input('输入行数：'))
for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*', end='')
    print()

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(0,row-i-1):
            print(' ',end='')
    for k in range(2*i+1):
            print('*',end='')
    print()

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(0,5-i):
        print(end=' ')
    for k in range(5-i,5):
        print('$',end='')
    print()

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(0,row-i-1):
            print(' ',end='')
    for k in range(i+1):
            print('*',end='')
    print()