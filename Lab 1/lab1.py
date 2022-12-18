############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

'''

This function returns the given value divided by 1.0. 

'''

def inverse(x):

    return 1.0/x

'''

First, this function creates a list of numbers between 0 and the given input.
Then, it creates a factorial of each value in the list while maintaining the list. 
The, it creates the inverses of each factorial, also while maintaining the list.
Finally, it adds all the numbers together in the list. 

'''

def add(x, y):

    return x + y

def e(n):

    range1 = list(range(n+1))

    map1 = list(map(factorial, range1))

    map2 = list(map(inverse, map1))

    reduce1 = reduce(add, map2)

    return reduce1

