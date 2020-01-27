#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:14:45 2020

@author: zishan
"""

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            if string[i:i+len(sub_string)]==sub_string:
                count += 1
                i += len(sub_string)
            else:
                i += len(sub_string)
                
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)