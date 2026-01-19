# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:53:38 2026

@author: Subash Chandar T
"""
##Introduction to python classes:
#       *classes are used to create our own object which has our specified data types .
#       *class keyword is used to create a class, next to the keyword , type/name for the object
#        to be given.
#       *class should contain the data attributes and the procedures (or) the implementation of the class , which can be 
#        given inside a function.
#       *class enables us to operate for different instances using the same class.
#       *We can create classes for our own need(i.e its all attributes and opertaions are defined by us for
#        our purpose).
#       *It is similar to functions in python.
    
    
    

# program for class object:

class coordinate(object):##defining a class 
    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval
    
    def distance(self,other):
        xdist=(self.x-other.x)**2
        ydist=(self.y-other.y)**2
        dist=(xdist+ydist)**0.5
        return dist

class coordinate2(object):
    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval
    def sqr(self,d):
        c=(self.x**d.x)+(self.y**d.y)
        return c
    
c=coordinate(5,2)
d=coordinate(4,3)

print(c.distance(d))#way of accessing the class 

c1=coordinate2(5,2)
d1=coordinate2(4,3)
print(c1.sqr(d1))
print(coordinate2.sqr(c1,d1))#another way for accessing class
