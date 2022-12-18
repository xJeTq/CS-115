############################################################
# Name: Anthony Curcio-Petraccoro 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# CS115 Lab 9 
############################################################

# ELIGIBLE FOR EXTRA CREDIT! 

from cs5png import PNGImage

def mult(c, n):
    '''Returns the value of c times n, but only uses addition. This is possible using a for loop.'''
    result = 0
    for x in range(n):
        x += 1
        result += c
    return result

#print("Mult:")
#print(mult(1.5, 28)) # Correct 
#print(mult(6, 7)) # Correct 

def update(c, n):
    '''Z starts at 0, and runs through the equation z^2 + c until all the values leading up to n not including n are met.'''
    z = 0
    for x in range(n):
        z = (z ** 2) + c
    return z

#print("Update:")
#print(update(1, 3)) # Correct 
#print(update(-1, 3)) # Correct 
#print(update(1, 10)) # Correct 
#print(update(-1, 10)) # Correct 

'''def inMSet(c, n):
    z = 0 
    for x in range(n):
        z = (z ** 2) + c
        if abs(z) > 2:
            return False
        else:
            return True'''

def inMSet(c, n):
    z = 0
    for x in range(n):
        z = (z ** 2) + c
        if abs(z) > 2:
            return False
    return True

#print("inMSet:") # Correct 
#print(inMSet(0 + 0j, 25)) # Correct 
#print(inMSet(3 + 4j, 25)) # Correct 
#print(inMSet(0.3 + -0.5j, 25)) # Correct 
#print(inMSet(-0.7 + 0.3j, 25)) # Correct 
#print(inMSet(0.42 + 0.2j, 25)) # Correct 

def weWantThisPixel(col, row):
    '''A function that returns True if we want the pixel at col, row and false otherwise.'''
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False

def test():
    '''A function to demonstrate how to create and save a png image.'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop in order to draw some pixels 

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file.

    image.saveFile()

    """If the condition statement is changed to 'if col % 10 or row % 10,' the function will no longer check if the grid is a square with height and width multiples of 10. Rather, it will return true if either the height or the width is a multiple of 10."""

def scale(pix, pixelMax, floatMin, floatMax):
    '''Pix, the current pixel column (or row) pixMax, the total number of pixel columns floatMin, the min floating-point value floatMax, the max floating-point value scale returns the floating-point value that corresponds to pix.'''
    return floatMin + (pix / pixelMax) * (floatMax - floatMin)

#print(scale(100, 200, -2.0, 1.0)) # Correct 
#print(scale(100, 200, -1.5, 1.5)) # Correct 
#print(scale(100, 300, -2.0, 1.0)) # Correct 
#print(scale(25, 300, -2.0, 1.0)) # Correct 
#print(scale(299, 300, -2.0, 1.0)) # Correct 

def mset():
    '''Creates a 300 x 200 image of the Mandlebrot set.'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop in order to draw some pixels.

    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = (x + y * 1j) 
            # Here is where you will need to create the complex number, c!
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file 

    image.saveFile() 

print(mset()) 
