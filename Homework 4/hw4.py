'''
Created on 10/13/2022
@author: Anthony Curcio-Petraccoro
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
CS115 - Hw 4
'''

def array_cat(L):
    '''This function concatenates the first and second spots of an array until there is nothing left to concatenate.'''
    if len(L) < 2:
        return []
    else:
        return [L[0] + L[1]] + array_cat(L[1:])

def pascal_row(n):
    '''This function returns one singular row of Pascal's Triangle, specifically the row inputted in the parameters.'''
    if n <= 0:
        return [1]
    else:
        last_row = pascal_row(n - 1)
        current_row = [1] + array_cat(last_row) + [1]
        return current_row

def pascal_triangle(n):
    '''This function returns pascals triangle up until the designated row provuided in the parameters.'''
    if n < 0:
        return []
    else:
        return pascal_triangle(n - 1) + [pascal_row(n)]
    
def test_pascal_row():
    '''This function tests the pascal_row function above.'''
    try:
        assert pascal_row(0) == [1]
        assert pascal_row(2) == [1, 2, 1]
        assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
        assert pascal_row(8) == [1, 8, 28, 56, 70, 56, 28, 8, 1]
        assert pascal_row(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    except AssertionError as message:
        print(message)
        raise AssertionError("Incorrect.")
        
def test_pascal_triangle():
    '''This function tests the pascal_triangle function above.'''
    try:
        assert pascal_triangle(0) == [[1]]
        assert pascal_triangle(1) == [[1], [1, 1]]
        assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
        assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    except AssertionError as message:
        print(message)
        raise AssertionError("Incorrect.")
    
