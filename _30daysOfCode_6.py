#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:47:43 2020

@author: zishan

"""
T = int(input("Enter the number of string :- "))
S=[]
for i in range(T):
    S.append(input(f"Enter your String {i} :- "))
print (S)

for i in S:
    print(f"{i[0::2]} {i[1::2]}")
