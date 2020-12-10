src1 = r'C:\Users\tangyingjin\Desktop\compare\bb'
src2 = r'C:\Users\tangyingjin\Desktop\compare\cc'




def compare(src1, src2):
    same = open('same.txt', 'w')
    try:
        with open(file=src1) as w:
            src1_content=set(w)

        with open(file=src2) as r:
            src2_content=set(r)

        with open('test.txt',mode='w') as result:
            for line in src1_content:
              if line not in src2_content:
                  result.write(line)
              else:
                  same.write(line)

        with open('test1.txt',mode='w')  as result1:
            for line in src2_content:
                if line not in src1_content:
                    result1.write(line)
                else:
                    same.write(line)
    except FileNotFoundError as e:
        print('error:{}'.format(e))


compare(src1, src2)
list1 = [1, 2, 3, 4, 5, 8]
list2 = [2, 3, 4, 6, 7, 8]
for i in range(len(list1)):
    for j in list2:
        if list1[i] == j:
            break
    else:
        print(list1[i])

    for z in list1:
        if list2[i] == z:
            break
    else:
        print(list2[i])
a = [x for x in list1 if x in list2]
b = [y for y in (list2 + list1) if y not in a]
# a两个列表中否存在
# b两个列表中的不同元素
# c在list1列表中而不再list2列表中
c = [x for x in list1 if x not in list2]
# d在list2中而不再list1中
d = [x for x in list2 if x not in list1]
