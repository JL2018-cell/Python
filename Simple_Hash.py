# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:34:21 2021

@author: npatlj
"""

import datetime
import math

def scnd(ls):
    return ls[1]

class myCache(object):
    def __init__(self):
        self.capacity = 5 #set capacity of cache = 5
        self.data = dict() #Use Python dictionary to store information.
    def get(self, item):
        if item not in self.data:
            print("Not found.")
        else:
            return self.data.dict[item]
    def put(self, key, value, weight):
        if len(self.data)>self.capacity:
            key_min = min(self.data.keys(), key=(lambda k: self.data[k][1]))
            print("Delete:",key_min)
            self.data.pop(key_min) 
        self.data[key] = [value, weight] #key = value, value = weight.
    def showSize(self):
        print(self.data)
        print("Size =",len(self.data))
    
tr = myCache()
tr.get("a")
tr.put("a",1,100)
tr.put("b",2,99)
tr.put("c",3,98)
tr.put("d",4,97)
tr.put("e",5,96)
tr.showSize()
tr.put("f",6,95)
tr.showSize()
tr.put("g",7,94)
tr.showSize()





