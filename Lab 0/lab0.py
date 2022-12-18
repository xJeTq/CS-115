############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 1
#  
############################################################

"""
I created two variables, one dedicated to the first letter of the word,
and one dedicated to the last letter of the word. I created an if statement
to see if the last and first letters matched. If they did, the function returns
true, if not, they return false. 
"""

def same(word):

    letter1 = word[0]
    letter2 = word[-1]

    if (letter1.lower()==letter2.lower()) :

        return True

    return False

"""
I created a function that input the variables into the equation listen on the
instructions sheet. It is imperative to use proper notation to make sure everything
is computer correctly. 
"""

def consecutiveSum(x, y):
    
    answer = (((x+y)/2)*(y-x-1))

    return answer

