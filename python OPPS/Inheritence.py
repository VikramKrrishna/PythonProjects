#Single inheritence
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is Child class")

obj = Child()
obj.fun2()
obj.fun1()
print("---------------------------")

#multilevel inheritence
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is Child class")
class Grandchild(Child):
    def fun3(self):
        print("This is Grandchild class")

obj = Grandchild()
obj.fun3()
obj.fun2()
obj.fun1()
print("---------------------------")

#Heirarchical inheritence
class Parent:
    def fun1(self):
        print("This is parent class")
class Child1(Parent):
    def fun2(self):
        print("This is Child1 class")
class Child2(Parent):
    def fun3(self):
        print("This is Child2 class")

obj = Child1()
obj.fun2()
obj.fun1()

obj = Child2()
obj.fun3()
obj.fun1()

print("---------------------------")

#Multiple inheritence
class Father:
    def fun1(self):
        print("This is Father class")
class Mother():
    def fun2(self):
        print("This is Mother class")
class Child(Father,Mother):
    def fun3(self):
        print("This is Child class")

obj = Child()
obj.fun3()
obj.fun2()
obj.fun1()
print("---------------------------")