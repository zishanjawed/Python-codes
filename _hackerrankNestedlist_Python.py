#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:30:20 2020

@author: zishan
"""

def fun(nameList,scoreList):
    """
n        input :- 
    """
    sorted_score = sorted((list(set(scoreList))))
    first = sorted_score[0]

    for i in sorted_score[1:]:
        if first == i:
            continue
        else:
            secound_value=i
            break
    index_value=[]
    for i in range(len(scoreList)):
        if secound_value == scoreList[i]:
            index_value.append(i)
    final_names= [nameList[i] for i in index_value]
    return sorted(final_names)

if __name__ == '__main__':
    nameList=[]
    scoreList=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameList.append(name)
        scoreList.append(score)
    ans=fun(nameList,scoreList)
    for i in ans:
        print(str(i))        