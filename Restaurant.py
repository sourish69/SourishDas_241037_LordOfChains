from Order import Order

class Restaurant:
    def __init__(self,name,x,y,category,dtime=0,ordList=[]):
        self.name=name
        self.x=x
        self.y=y
        self.category=category


    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getName(self):
        return self.name

    def acceptOrder(self):
        print("Thank you for choosing "+self.name+" ! Your order has been confirmed.")
        

    def rejectOrder():
        print("Oops! We cannot deliver your order")


    def calcTime(self,orders):
        time=0
        for i in orders:
            time+=20
        print("Delivery Time: " + str(time) + " minutes")

    