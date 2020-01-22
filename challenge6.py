#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:30:18 2020

@author: zishan

Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 
"""
import math
def formula (D,C=50,H=30):
    """
    input:
        C and H is fixed
        D is a numbers saprated with coma 
    return:
        Q :list of number calculated by Q = sqare root of [(2*C*D)/H]
    """
    list_num = D.split(',')
    num_list = [i for i in list_num]
    Q = []
    for i in num_list:
        Q.append(str(int(round(math.sqrt((2*C*float(i))/H)))))
    return Q
    
    
row_input=input("Enter your numbers saprated by ',' :- ")    
ans= formula(row_input)
print(','.join((ans)))
