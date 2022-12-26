#Super Keyword
class A:
    def __init__(self):
        print("This is Class A")
    def fun1(self):
        print("This is fun1")

class B(A):
    def __init__(self):
        print("This is Class B")
        super().__init__()
    def fun1(self):
        print("This is fun1")

obj = B()