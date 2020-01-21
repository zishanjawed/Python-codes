#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:29:59 2020

@author: zishan

Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def factor(num):
    if num == 1:
        return num
    else :
        return num*factor(num-1)

num = int(input("Enter the Number :- "))
print("The factorial is :- ",factor(num))