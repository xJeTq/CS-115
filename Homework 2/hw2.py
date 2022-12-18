'''
Created on 9/26/2022
@author:   Anthony Curcio-Petraccoro & Alex Coroian 
Pledge:    I pledge that I have abided by the Stevens Honor System. 
CS115 - Hw 2
'''

import sys 
from functools import reduce

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    #Returns the score of the letter given.
    if len(scorelist) == 0:
        return 0
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    #Returns the score of a word by finding the score of each letter and adding them together.
    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def ind(e, L):
    #Searches a string or a list and returns it's index value. 
    if L == []:
        return 0
    elif L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def checkWord(word, Rack):
  #Checks to see if the contents in rack can make a word. 
  if word == "":
    return True
  if word[0] in Rack:
    indRack = ind(word[0], Rack)
    return checkWord(word[1:], Rack[0: indRack] + Rack[indRack + 1:])
  else:
    return False
 
def scoreList(Rack):
  #Takes a list of letters and creates a combination of words in the dictionary and returns their Scrabble value. 
  
  words = filter(lambda y : checkWord(y, Rack), Dictionary)
  finalList = map(lambda y: [y, wordScore(y, scrabbleScores)], words)
  return list(finalList)
 
def findBigger(s1, s2):
  #Returns the greater of two given values. 
  
  if s1[1] > s2[1]:
    return s1
 
  return s2

def bestWord(Rack):
  #Returns the word with the highest score. 
  
  allWords = scoreList(Rack);
  return reduce(lambda w, c: findBigger(w, c), allWords, ["", 0])
