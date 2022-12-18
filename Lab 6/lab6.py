'''
Created on 10/19/2022
@author:   Anthony Curcio-Petraccoro
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Lab 6
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    else:
        return False

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n <= 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1' 
    else:
        return numToBinary(n // 2) + '0' 

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s. 
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s[0] == '1':
        return (2 ** (len(s)-1)) + binaryToNum(s[1:]) 
    else:
        return binaryToNum(s[1:])

def zero(n):
    '''Concatenates or slices 0s at the beginning of a string to ensure it's eight digits long.'''
    if len(n) == 8:
        return n
    elif len(n) < 8:
        return  zero('0' + n)
    else:
        return zero(n[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits. 
    Returns the binary representation of binaryToNum(s) + 1.'''
    num1 = binaryToNum(s) + 1
    num2 = numToBinary(num1)
    return zero(num2)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n <= 0:
        return ''
    else:
        return count(increment(s), n - 1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative. 
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n <= 0:
        return ''
    elif n % 3 == 2:
        return numToTernary(n // 3) + '2'
    elif n % 3 == 1:
        return numToTernary(n // 3) + '1' 
    else:
        return numToTernary(n // 3) + '0' 

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s[0] == '2':
        return ((3 ** (len(s))) + ternaryToNum(s[1:])) - (3 ** (len(s) - 1))# Wrong 
    elif s[0] == '1':
        return (3 ** (len(s) - 1)) + ternaryToNum(s[1:]) 
    else:
        return ternaryToNum(s[1:])
