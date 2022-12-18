'''
Created on 10/5/2022
@author: Anthony Curcio-Petraccoro
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 3
'''
from functools import reduce
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(numberOfCoins, listOfCoins):
    '''This function returns the least amount of coins that makes up the desired value, and returns the list.'''
    if numberOfCoins < 1:
        return [0, []]
    elif listOfCoins == []:
        return [float("inf"), []]
    elif listOfCoins[-1] > numberOfCoins:
        return giveChange(numberOfCoins, listOfCoins[:-1])
    else:
        useIt = giveChange(numberOfCoins - listOfCoins[-1], listOfCoins)
        useIt[0] += 1
        useIt[1] += [listOfCoins[-1]]
        loseIt = giveChange(numberOfCoins, listOfCoins[:-1])
        return min(useIt, loseIt)

print(giveChange(69, [1, 5, 10, 25, 50]))

# Here's the list of letter values and a small dictionary to use. 
# Leave the following lists in place. 

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def explode(S):
    '''Separates a given string or list into different elements, then inputs them
into a list.'''
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])

def letterScore(letter, scorelist):
    '''Returns the score of the letter given.'''
    if len(scorelist) == 0:
        return 0
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''Returns the score of a word by finding the score of each letter and adding them together.'''
    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordsWithScore(dct, scores):
    '''Returns a list of words in dct, with their Scrabble score.'''
    if len(dct) == 0:
        return []
    else:
        return [[dct[0], reduce(lambda x, y: x + letterScore(y, scores), explode(dct[0]), 0)]] + wordsWithScore(dct[1:], scores)

    '''Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def take(n, L):
    '''Returns the list from the 0 index to the n index, assuming L is a list and n is at least 0.'''
    if len(L) < n:
        return L
    elif n == 0: 
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list n index to the last index in the list, assuming L is a list and n is at least 0.'''
    if len(L) < n:
        return []
    elif n == 0:
        return L
    elif n == len(L) - 1:
        return [L[-1]]
    else:
        return [L[n]] + drop(n + 1, L)

