#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:05:59 2020

@author: zishan
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    reqired_marks=list(student_marks[query_name])
    ans = 0
    for i in reqired_marks:
        ans += i
    print("%.2f"%ans)