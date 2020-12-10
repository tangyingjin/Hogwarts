from hogwarts.sdet.Student import Student
def  num():
    print(2+2)

def x(a,b=1,*c,**d):
    print(f'a={a}\n',f'b={b}\n',f'c={c}\n',f'd={d}\n')
x(1,2,3,3,x=1,y=2)
#=归为字典,*c可变长的参数，**d词典

#类
class MyClass:
    i=12345
    def func(self):
        return 'hello world'
x=MyClass()
print(x.func())

Student()