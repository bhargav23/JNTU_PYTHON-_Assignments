# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:54:21 2020

@author: kiran
"""

#List of Product objects
class Product:
    def __init__(self, name, pid,price,manufacturer_name):
        self.pid = pid  
        self.name = name 
        self.price = price 
        self.manufacturer_name = manufacturer_name

        print("This is Product constructor")

    def __repr__(self):
        return self.pid+"\t"+str(self.name)+"\t"+self.price+"\t"+str(self.manufacturer_name)

    def __hash__(self):
        return hash((self.pid, self.name))

    def __eq__(self, obj):
        return isinstance(obj, Product) and obj.pid == self.pid

    def __ne__(self, obj):
        return not self == obj

    def met(self):
        print("This is met in Product class: "+self.pid+"\t"+str(self.name))
# creating list
list1 = []

# appending instances to list
list1.append( Product(40,"Coffee",10,"Nescafe") )
list1.append( Product(20,"Milk", 20,"Heritage") )
list1.append( Product(1,"Bread",5,"Parle") )
list1.append( Product(3,"Chocolate",8,"Dairy Milk") )
list1.append( Product(3,"Chocolate",8,"Dairy Milk") )

def Show(lst):
    for i in lst:
        print(i.name, i.pid,i.price,i.manufacturer_name)
        
print("\n")
for obj in list1:
    obj.met()


print("Before Sorting : ")

Show(list1)

list1.sort(key=lambda x: x.price)

print("Sorting Based on price : ")

Show(list1)

print("Sorting Based on price in reverse order :")
list1.sort(reverse=True,key=lambda x: x.price)
Show(list1)

print("Using Set function :")

slist1 = set(list1)
Show(slist1)



