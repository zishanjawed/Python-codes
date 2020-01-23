#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:26:43 2020

@author: zishan
"""
n = int(input())
d= {}
for i in range(n):
    x = input().split()
    d[x[0].lower()]=x[1]

while True:
    try:
        name=input()
        if name in d.keys():
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break