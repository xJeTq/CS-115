#
# life.py - Game of Life lab
#
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# Date: 11/16/2022 
#

import random
import sys

def createOneRow(width):
    '''Returns one row of zeros of width "width"... You should use this in your createBoard(width, height) function.'''
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''Returns the proper height and width of the board, but in a 2D array.'''
    board = []
    for row in range(height):
        board += [createOneRow(width)]
    return board

A = createBoard(5, 3)
#print(A) - Correct 

def printBoard(A):
    '''Prints a board of 0s with the proper height and width, this time not in a 2D array.'''
    board = ''
    for row in A:
        for col in row:
            board += str(col)
        board += '\n'
    print(board)

#printBoard(A) - Correct

def diagonlize(width, height):
    '''Creates an empty board then modifies it so that it has a diagonal strip of "on" cells'''
    B = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                B[row][col] = 1
            else:
                B[row][col] = 0
    return B 

B = diagonlize(7, 6)
#print(B) - Correct
#printBoard(B) - Correct

def innerCells(width, height):
    '''Creates all the inner cells as 1s, and leaves the outer edge to remain 0s.'''
    C = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row != 0 and row != width - 1:
                if col != 0 and col != height - 1:
                    C[row][col] = 1
            else:
                C[row][col] = 0
    return C

C = innerCells(5, 5)
#printBoard(C) - Correct

def randomCells(width, height):
    '''Randomly generates a 0 or 1 in the inner cells of the 2D array, leaving the outside of the 2D array to remain 0s.'''
    D = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row != 0 and row != width - 1:
                if col != 0 and col != height - 1:
                    D[row][col] = random.choice([0, 1])
            else:
                D[row][col] = 0
    return D

D = randomCells(10, 10)
#printBoard(D) - Correct

'''
Copy Test (Original): - Incorrect 
oldA = createBoard(2, 2)
printBoard(oldA)
newA = oldA
oldA[0][0] = 1
printBoard(oldA)
printBoard(newA)
'''

def copy(E):
    '''Instead of overwriting the original 2D array, this function allows you to keep the contents of the original 2D array and edit the new one by perforing a "Deep Copy."'''
    lenRow = len(E)
    lenCol = len(E[0])
    newE = createBoard(lenRow, lenCol)
    for row in range(lenCol):
        for col in range(lenRow):
            E[row][col] = newE[row][col]
    return newE

'''
Copy Test (With Function): - Correct 
oldA = createBoard(2, 2)
printBoard(oldA)
newA = copy(oldA)
printBoard(newA)
oldA[0][0] = 1
printBoard(oldA)
printBoard(newA)
'''

def innerReverse(F):
    '''Since the outer edge is always 0, reverses the numbers on the inside. It will copy the original 2D array, but reverse each number. The original 2D array will still exist.'''
    lenRow = len(F)
    lenCol = len(F[0])
    newF = createBoard(lenRow, lenCol)
    for row in range(lenCol):
        for col in range(lenRow):
            if row != 0 and row != lenRow - 1:
                if col != 0 and col != lenCol - 1:
                    if F[row][col] == 1:
                        newF[row][col] = 0
                    else:
                        newF[row][col] = 1
    return newF

'''
InnerReverse Test (With Function): - Correct 
F = randomCells(8, 8)
printBoard(F)
newF = innerReverse(F)
printBoard(newF)
'''

def countNeighbors(row, col, G):
    '''Count the amount of 1s next to a certain cell in a given 2D array.'''
    count = 0
    if G[row][col] == 1:
        count += -1
    for x in range(col - 1, col + 2):
        for y in range(row - 1, row + 2):
            if G[y][x] == 1:
                count += 1
    return count 

def next_life_generation(G):
    '''Makes a copy of G and then advances one generation of Conway's game of life within the *inner cells* if that copy. The outer edge always stays a 0.'''
    lenRow = len(G)
    lenCol = len(G[0])
    newG = createBoard(lenRow, lenCol)
    for row in range(1, lenCol - 1):
        for col in range(1, lenRow - 1):
            var = countNeighbors(row, col, G)
            if G[row][col] == 1:
                newG[row][col] = 1
            if var < 2:
                newG[row][col] = 0
            if var > 3:
                newG[row][col] = 0
            if G[row][col] == 0 and var == 3:
                newG[row][col] = 1
    return newG 

'''
Generation Test: - Correct 
G = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
printBoard(G)
G2 = next_life_generation(G)
printBoard(G2)
G3 = next_life_generation(G2)
printBoard(G3)
'''
