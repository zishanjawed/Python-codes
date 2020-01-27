#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:02:52 2020

@author: zishan
"""

def split_and_join(line):
    # write your code here
    ans = line.split(" ")
    return "-".join(ans)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)