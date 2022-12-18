############################################################ 
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 4 
############################################################

def knapsack(capacity, items):
    #Knapsack returns a list of the maximum value of the items under the capacity condition. Returns the sum of the values, and the item itself, which contains the individual value and the weight.  
    if len(items) < 1:
        return [0] + [items]
    elif capacity < 1:
        return [0] + [[]] 
    elif items[-1][0] > capacity:
        return knapsack(capacity, items[:-1])
    else:
        useIt = knapsack(capacity - items[-1][0], items[:-1])
        useIt[0] += items[-1][-1]
        useIt[1] += [items[-1]]
        loseIt = knapsack(capacity, items[:-1])
        return max(useIt, loseIt)
