d={'mike':10,'lucy':2,'ben':30}
for i in d.values():
    print(i)
i=d.items()
# 查看对象的类型
print(type(i))
map(lambda x:x%2==0,[1,2,3])

i=sorted(d.items(),key=lambda x:x[1])
print(i)

dict=[('mike', 10), ('lucy', 2), ('ben', 30)]
for d in dict:
    print(d[1])
[ lambda x:x*x(x) for x in range(10)]
