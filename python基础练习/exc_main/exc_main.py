from python基础练习.exc_main import exc_main_test
from python基础练习.exc_main import exc_main_test1

print(exc_main_test.get_sum(1, 2))
print(exc_main_test1.get_sum(1, 2))


# todo:import导入文件时，会自动把所有暴露在外面的代码全都执行了一遍。因此，如果你要把一个东西封装成一个模块，又想让它可以执行的话，你必须将要执行的代码放在if __name__='__main_'下面