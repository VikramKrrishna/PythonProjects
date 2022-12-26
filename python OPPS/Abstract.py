from abc import ABC,abstractmethod
class A(ABC): #Abstract
    @abstractmethod
    def display(self):
        None #Only declaration not defination
    @abstractmethod
    def show(self):
        None
    
class B(A): # concreat class
    def display(self):
        print("Absract Method")
    def show(self):
        print("Show Method")


class C(A): #Abstract class
    def display(self):
        print("Absract Method")

#We not instatiate the object for anstract class

obj = B()
obj.display()
obj.show()