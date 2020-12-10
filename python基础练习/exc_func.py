class A:
    def __init__(self):
        print("enter A")


class B(A):
    def __init__(self):
        print("enter B")
        A.__init__(self)

B()
