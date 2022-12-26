#Method overloading
#same class
#same function or method
#different parameters

class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c

obj = A()
print(obj.sum(1,2,5))


#Method overriding
#different class
#same function or method names
#different parameters

class A:
    def display(self):
        print("This is class A")
class B(A):
    def display(self):
        print("This is class B")
        super().display()
obj = B()
print(obj.display())