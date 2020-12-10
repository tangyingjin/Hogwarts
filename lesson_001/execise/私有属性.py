class Student(object):
    @property
    def socre(self):
        return self.sorce

    @socre.setter
    def socre(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be integer!')
        elif value <0 or value >100:
            raise ValueError('value must be 0-100!')
        self.sorce=value




s=Student()
s.socre=40
print(s.socre)
s.socre
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
        @property
        def width(self):
            return self._value

        @width.setter
        def width(self,value1):
            if not isinstance(value1,int):
                raise ValueError("vlaue must be integer")
            elif value1<0:
                raise ValueError("value must be int")
            self._value=value1

        @property
        def height(self):
            return self._value

        @height.setter
        def height(self,value):
            if not isinstance(value,int):
                raise ValueError("value must be integer")
            elif value<0:
                raise ValueError("value must be int")
            self._value=value

        @property
        def resolution(self):
            return self._value*self._value
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')