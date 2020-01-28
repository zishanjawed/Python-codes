#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:20:41 2020

@author: zishan
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
class Test():
    
    def __init__(self):
        string=''
        
    
    def getString(self):
        self.string = input ("Please Enter Some text :- ")
    
    
    def printSrting(self):
        print(self.string.upper())
        
obj1=Test()
obj1.getString()
obj1.printSrting()
            

