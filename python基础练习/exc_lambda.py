# s=map(lambda x:x*2 ,[1,2,34,5])
# for i in s:
#  print(i)
from functools import reduce

# var=filter(lambda x:x%2==0,[2,4,8,9])
# for y in var:
#     print(y)
#
var1=reduce(lambda x,y:x*y,[1,2,3,5])
print(var1)

