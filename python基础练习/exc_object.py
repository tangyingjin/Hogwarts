class A:
    def __init__(self, a, b):
        print("enter A")
        self.a = a
        self.b = b

    def get_params(self):
        print('pass')


class B(A):
    def set_params(self):
        print(self.a + self.b)


B(1, 2)


class C(A):
    def __init__(self, a, b, c):
        print("enter B")
        super().__init__(a, b)
        self.c = c

    def set_params(self):
        print(self.a + self.b + self.c)


C(1,2,3)

class D(A):
    def __init__(self,c):
        self.c=c

    def set_params(self):
        print(self.a + self.b + self.c)

D(1)

class E(A):
    def __init__(self,*args):
        super().__init__(*args)
        print(super())


print(E(1, 2))
print(E(1,2).a)
# todo:init表示构造函数，意即一个对象生成时会被自动调用的函数
# todo:如果子类继承父类，子类没有重写构造函数，那么子类的构造函数会自动继承父类的构造函数。例如上面的B()
# todo:如果子类继承父类，子类重写构造函数，而且你又需要父类的构造函数；这时你需要显示的调用父类的构造函数，super().__init__().liru
# todo:如果子类继承父类，不显示的调用父类的构造函数，是不会自动调用的。例如D()只有一个参数c，并没有调用父类的a,b参数
class Document:
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    #     __开头是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]
#     todo:在类的函数内部可以访问私有属性



harry_book = Document('harry', 'J.k', 'I love you....')
print(harry_book.get_context_length())
harry_book.intercept_context(8)
# harry_book.__context
# todo:实例化的对象不能访问私有属性，私有属性，是指不需要在类的函数之外的地方被访问和修改的属性
print(harry_book.get_context_length())


# todo:那么父类的私有属性，能否被子类继承吗？不可以被子类继承
class Entity(Document):
      pass
i=Entity('s','t','s errr')
i.intercept_context(3)
print(i.get_context_length())


class Base:
    def __init__(self):
        print('enter Base')
        print('leave Base')

class A(Base):
    def __init__(self):
        print('enter A')
        super().__init__()
        print('leave A')

class B(Base):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')

class C(A,B):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')

c=C()

print(C.mro())


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        # super().__init__(object_type)
        self.title = title
        self.author = author
        self.__context = context



    def get_context_length(self):
        return len(self.__context)

    def get_object_type(self):
        print(self.object_type)

book=Document('a','abc','w','e')
book.get_context_length()
book.print_title()
print(book.object_type)
print(book.get_object_type())


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())


class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')

print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))




