e=1
try:
        1/0
except ZeroDivisionError as e:
        print('error：{}'.format(e))
# print(e)
#运行上面代码，执行结果 NameError: name 'e' is not defined
# 官方文档说明：
# except E as N:
#      foo
# 就等于
# except E as N:
#     try:
#         foo
#     finally:
#         del N
# 因为上面例子的e最后被delete，所以会抛NameError

import  datetime
print(datetime.datetime.now())