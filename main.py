from Restaurant import Restaurant
from Order import Order
from Customer import Customer
from Delivery import Delivery

import random
import string
import math


def calcDistance(x1,x2,y1,y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def createRestaurants():
    for i in range(6):
        restaurants.append(Restaurant(resnames[i],random.randrange(0,100),random.randrange(0,100),categories[random.randrange(0,3)]))

global categories,restaurants,resnames,delnames
global indmenu,chimenu,contimenu
global orders

indmenu=["Butter Chicken","Biryani","Mutton Curry","Dal Makhani","Paneer Tikka"]
chimenu=["Hot and Sour Chicken","Chopsuey","Chicken Sui Mai","Duck Fried Rice","Wonton Soup"]
contimenu=["Stroganoff","Lasagna","Steak","Pastrami","Risotto"]

restaurants=[]
orders=[]

categories=["Indian","Chinese","Continental"]
resnames=["Saffron","Peshawari","Mocambo","Tamarind","Lotus","Spice"]
delnames=["DB1","DB2","DB3","DB4","DB25","DB6"]


name=input("Hello! Please enter your name \n")
x=int(input("Please enter your x-coordinate \n"))
y=int(input("Please enter your y-coordinate \n"))
     
cust1=Customer(name,x,y)

createRestaurants()

selected=[]
finalRest=""

choice=int(input("Press 1 to order Indian Food, Press 2 to order Chinese Food, Press 3 to order Continental Food \n"))

if choice == 1:
    for i in restaurants:
        if i.category == "Indian":
            selected.append(i)
            print(i.getName() + " is available, and located " + str(round(calcDistance(x, i.getX(), y, i.getY()),1)) + " kilometres from you\n")
    
    if selected:
        finalRest = input("Select the restaurant from which you would like to order!\n")
        for i in selected:
            if i.getName() == finalRest:
                print("Menu: ")
                for j in indmenu:
                    print(j)
                while(True):
                    foodc=input("Enter item or type STOP to finish \n")
                    if(foodc=="STOP"):
                        break
                    else:
                        orders.append(foodc)
                i.acceptOrder()
                order=Order(''.join(random.choices(string.ascii_lowercase, k=5)),"Indian","PREPARING",0,orders)
                order.calcCost()
                #i.assignDB()
                db=Delivery(random.randrange(0,100),random.randrange(0,100))
                db.acceptOrder()
                order.setStatus("TO BE DELIVERED")
                i.calcTime(orders)
                print("Status: " + order.status)
    else:
        print("No Indian restaurants found near you.")
    
if choice == 2:
    for i in restaurants:
        if i.category == "Chinese":
            selected.append(i)
            print(i.getName() + " is available, and located " + str(round(calcDistance(x, i.getX(), y, i.getY()),1)) + " kilometres from you\n")
    
    if selected:
        finalRest = input("Select the restaurant from which you would like to order! \n")
        for i in selected:
            if i.getName() == finalRest:
                print("Menu: ")
                for j in chimenu:
                    print(j)
                while(True):
                    foodc=input("Enter item or type STOP to finish \n")
                    if(foodc=="STOP"):
                        break
                    else:
                        orders.append(foodc)
                i.acceptOrder()
                order=Order(''.join(random.choices(string.ascii_lowercase, k=5)),"Chinese","PREPARING",0,orders)
                order.calcCost()
                #i.assignDB()
                db=Delivery(random.randrange(0,100),random.randrange(0,100))
                db.acceptOrder()
                order.setStatus("TO BE DELIVERED")
                i.calcTime(orders)
                print("Status: " + order.status)
    else:
        print("No Chinese restaurants found near you.")

if choice == 3:
    for i in restaurants:
        if i.category == "Continental":
            selected.append(i)
            print(i.getName() + " is available, and located " + str(round(calcDistance(x, i.getX(), y, i.getY()),1)) + " kilometres from you\n")
    
    if selected:
        finalRest = input("Select the restaurant from which you would like to order!\n")
        for i in selected:
            if i.getName() == finalRest:
                print("Menu: ")
                for j in contimenu:
                    print(j)
                while(True):
                    foodc=input("Enter item or type STOP to finish \n")
                    if(foodc=="STOP"):
                        break
                    else:
                        orders.append(foodc)
                i.acceptOrder()
                order=Order(''.join(random.choices(string.ascii_lowercase, k=5)),"Continental","PREPARING",0,orders)
                print("Order ID: " + order.uid + " Status: " + order.status)
                order.calcCost()
                db=Delivery(random.randrange(0,100),random.randrange(0,100))
                db.acceptOrder()
                order.setStatus("TO BE DELIVERED")
                i.calcTime(orders)
                print("Order ID: " + order.uid + " Status: " + order.status)
    else:
        print("No Continental restaurants found near you.")


