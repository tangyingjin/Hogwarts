class Animal():
    def __init__(self, sex, height, weight):
        self.__sex = sex
        self.height = height
        self.weight = weight

    def say_hello(self):
        raise Exception('say hello not implemented')

    def get_sex(self):
        # print('Achieve sex information for parent method:{}'.format(self.__sex))
         return self.__sex
#父类创建方法返回私有属性的值，然后子类调用父类方法去取得该私有属性的值
class Person(Animal):
        def __init__(self,name,age):
            super().__init__('M',171,100)
            self.name=name
            self.age=age

        def say_hello(self):
            print('hello,{},age:{},weight:{},is sex:{}'.format(self.name,self.age,self.weight,self.get_sex()))
            print('sex:{}'.format(self._Animal__sex))
#只有透过self._Parent__varname去读取私有属性的值
john=Person('john',25)
john.say_hello()
john.get_sex()

# todo:子类不能继承父类的私有属性，只有透过self._Parent__varname去读取私有属性的值，或在父类创建方法返回私有属性的值，然后子类调用父类方法去取得该私有属性的值