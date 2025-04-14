class Order:
    def __init__(self,uid,ocategory,status,cost,orderList):
        self.uid=uid
        self.ocategory=ocategory
        self.status=status
        self.orderList=orderList
        self.cost=cost


    def checkStatus(self):
        return self.status
    
    def setStatus(self,status):
        self.status=status
    
    def calcCost(self):
        cost=0
        if self.ocategory=="Indian":
            for i in self.orderList:
                if i=="Butter Chicken":
                    cost+=250
                if i=="Biryani":
                    cost+=350
                if i=="Mutton Curry":
                    cost+=525
                if i=="Dal Makhani":
                    cost+=150
                if i=="Paneer Tikka":
                    cost+=200
                
        if self.ocategory=="Chinese":
            for i in self.orderList:
                if i=="Hot and Sour Chicken":
                    cost+=275
                if i=="Chopsuey":
                    cost+=400
                if i=="Chicken Sui Mai":
                    cost+=225
                if i=="Duck Fried Rice":
                    cost+=375
                if i=="Wonton Soup":
                    cost+=200

        if self.ocategory=="Continental":
            for i in self.orderList:
                if i=="Stroganoff":
                    cost+=275
                if i=="Lasagna":
                    cost+=325
                if i=="Steak":
                    cost+=500
                if i=="Pastrami":
                    cost+=375
                if i=="Risotto":
                    cost+=250
            
        self.cost=cost
        print("Your total cost is: " + str(cost))
        
    



