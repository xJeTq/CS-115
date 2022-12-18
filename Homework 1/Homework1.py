############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Homework #1 
#  
############################################################

from functools import reduce 

'''
This function simply multiples two inputs together. 
'''

def mult(x, y):

    return x * y

'''
This function simply adds two inputs together.
'''

def add(x, y):

    return x + y

'''
This function creates a list of all numbers ranging from 1 to the input value.
It then multiplies them together. 
'''

def factorial(n):

    FactorialRange1 = list(range(1, n+1))

    return reduce(mult, FactorialRange1)

'''
This function gathers the length of a given array or list.
It then adds all the numbers together in the list, and divides by the list count,
giving you the mean of the list. 
'''

def mean(L):

    IntegerCount = len(L)

    MeanAdd = reduce(add, L)

    return MeanAdd / IntegerCount
