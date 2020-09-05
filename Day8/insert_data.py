# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:10:59 2020

@author: siram
"""

import json
from pymongo import MongoClient
myclient = MongoClient()

mydb = myclient["jntuk"]
mycol = mydb["staff"]

# reading the file
with open('realestate.json')  as f:
    # returns JSON object as  
    # a dictionary 
    data = json.load(f) 
    

### inserting all the records
x = mycol.insert_many(data)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

## select query ( displaying all the records)
for x in mycol.find():
    print(x)
    print("--------------")
