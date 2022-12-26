#Scope public
class Encap():
    a = 10
    def Display(self):
        print("Welcome")

obj = Encap()
#print(obj.a)
#obj.Display()

#Scope private
class Encap():
    __a = 10 #private variable
    def Display(self): #private method
        print("Welcome")
        print(self.__a)
    
obj = Encap()
#print(obj.a)
obj.Display()