############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 3
############################################################

def change(amount, coins):
    '''This function takes an input of an amount, and a list of coin values.
It returns the least amount of coins needed to obtain the given amount. If there
are no coins given, it returns float("inf")'''
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[-1] > amount:
        return change(amount, coins[:-1])
    else:
        useIt = 1 + change(amount - coins[-1], coins)
        loseIt = change(amount, coins[:-1])
        return min(useIt, loseIt)
print(change(131, [1, 5, 10, 20, 50, 100]))
