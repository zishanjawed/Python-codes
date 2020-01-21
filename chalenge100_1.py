#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 01:00:05 2020

@author: zishan

Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""
nums=[]
f=', '
for i in range(2000,3201,):
    if (i%7==0) and (i%5!=0):
        nums.append(i)
print(f.join(str(x) for x in nums))
