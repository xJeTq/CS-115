'''
Created on 10/24/2022
@author:   Anthony Curcio-Petraccoro
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 5 
'''

luc = {}

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in luc:
        return luc[n]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        luc[n - 1] = fast_lucas(n - 1)
        luc[n - 2] = fast_lucas(n - 2)
        return luc[n - 1] + luc[n - 2]

memo = {}

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if (amount, tuple(coins)) in memo:
        return memo[(amount, tuple(coins))]
    if amount <= 0 and coins == []:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[-1] > amount:
        return fast_change(amount,(coins[:-1]))
    else:
        useIt = 1 + fast_change(amount - coins[-1], coins)
        loseIt = fast_change(amount, coins[:-1])
        memo[(amount, tuple(coins))] = min(useIt, loseIt)
        return memo[(amount, tuple(coins))]

# If you did this correctly, the results should be nearly instantaneous.
print("fast_lucas results:")
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123
print("fast_change results:")
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))
