#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:20:16 2020

@author: zishan
"""

from functools import reduce
import operator

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

#Using list Comprihension 
print([str(names).upper() for names in my_pets])

#Using map() function
print(list(map(lambda names : str(names).upper(),my_pets)))

#Using Normal function with map()
def to_upper(name):
    return str(name).upper()
print(list(map(to_upper, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_value= (list(zip(my_strings,my_numbers)))
#sorting using the secound index of tuple
sorted_my_value= sorted(my_value,key= lambda x : x[1])
print(sorted_my_value) #by default sorted sort from lowest to highest

#sorting reverse using reverce = True
print(sorted(my_value,key = lambda x:x[1], reverse=True))

#sorting using the secound index of tuple in reverce 
reverse_sorted_my_value= reversed(sorted_my_value)
print(reverse_sorted_my_value) #list_reverseiterator object
print(list(reverse_sorted_my_value))

#reversing using the conept of itemgetter
print(sorted(my_value,key= operator.itemgetter(1)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda num: num > 50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#reduce required one function or lambda expression and itrables 
print(reduce(lambda x,y:x+y, my_numbers, scores))