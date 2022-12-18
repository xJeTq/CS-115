############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 2 
#  
############################################################

def dot(L, K):
    '''Finds the dot products of L and K. Multiples the corresponding points
in L and K, then adds the different points together.'''
    if L == []:

        return 0

    else:
        
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    '''Separates a given string or list into different elements, then inputs them
into a list.'''
    if S == "":
        return []

    else:
        return [S[0]] + explode(S[1:])



def ind(e, L):
    '''Takes a given variable and searches for it within a list or string. Then outputs
the location of the given variable.'''
    if L == "":

        return 0

    if L == []:

        return 0

    if L[0] == e:

        return 0
        
    else:

        return ind(e, L[1:]) + 1



def removeAll(e, L):
    '''Removes the given variable from the given list or string.'''
    if L == []:

        return []

    if L[0] == e:

        return removeAll(e, L[1:])

    else:

        return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    '''Takes a fucntion and a list, and performs the given function on the list and
outputs the new list.'''
    if L == []:

        return []

    if f(L[0]):

        return [L[0]] + myFilter(f, L[1:])
    
    else:

        return myFilter(f, L[1:])
    

def deepReverse(L):
    '''Reverses every element in a list, even if the element is also a list.'''
    if L == []:

        return L

    elif isinstance(L[0], list):

        return deepReverse(L[1:]) + [deepReverse(L[0])]
    
    else:
    
        return deepReverse(L[1:]) + [L[0]]


