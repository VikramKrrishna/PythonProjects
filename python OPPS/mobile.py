class Mobile:
    def __init__(self,Brand,Battery,RAM,Camara,Price):
        self.Br = Brand
        self.Ba = Battery
        self.Ra = RAM
        self.Ca = Camara
        self.Pr = Price
    
    def display(self):
        print("\nBrand:",self.Br)
        print("Battery:",self.Ba)
        print("RAM:",self.Ra)
        print("Camara:",self.Ca)
        print("Price:",self.Pr)
        print("----------------------")

obj = Mobile("Nokia","5000mah","16GB","48mp","50000")
obj.display()

obj = Mobile("OOneplus","5000mah","32GB","108mp","90000")
obj.display()

