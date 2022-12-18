''' 
Created on 10/31/2022 
@author:   Anthony Curcio-Petraccoro & Devin Yun 
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 6 
''' 
# I AM ELIGBLE FOR EXTRA CREDIT! 
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 7 

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(t, i = 0):
    '''Precondition: s is a string of 0s and 1s. 
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if t == 0:
        return '0' * (COMPRESSED_BLOCK_SIZE - i)
    else:
        add = '0' if t % 2 == 0 else '1'
        return numToBinary(t // 2, i + 1) + add

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s. 
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s[0] == '1':
        return (2 ** (len(s)-1)) + binaryToNum(s[1:]) 
    else:
        return binaryToNum(s[1:])
    
def compress(s, length = 0, output = '0'):
    '''Takes in a binary string of length 64 and returns another binary string
as the output.'''
    #The largest number this algorithm could compress is a number which compresses to 64  ones. 
    if s == '':
        if length != 0:
            t = numToBinary(length)
            return t
        else:
            return ''
    if length == MAX_RUN_LENGTH or output != s[0]:
        t = numToBinary(length)
        if output == '1':
            return t + compress(s, 0, '0')
        else:
            return t + compress(s, 0, '1')
    else:
        return compress(s[1:], length + 1, output)
    
def uncompress(s, length = '', output = '0'):
    '''Takes in a binary string of any length and returns another binary string of length 64'''
    current = s[0:COMPRESSED_BLOCK_SIZE]
    size = int(current, 2)
    length += output * size
    s = s[COMPRESSED_BLOCK_SIZE:]
    if output == '0':
        output = '1'
    else:
        output = '0'
    if len(s) == 0:
        return length
    else:
        return uncompress(s, length, output)

def compression(s):
    '''Divides the length of the compressed image by the uncompressed length.'''
    return (len(compress(s)) / len(s))

#print(compression("0000000000000000000000000000000011111111111111111111111111111111"))
#The ratio of '0' * 32 and '1' * 32 is 0.46875
#print(compression('0' * 64))
#The ratio of '0' * 64 is 0.390625 
#print(compression('1' * 64))
#The ratio of '1' * 64 is 0.46875 

#It isn't always possible to compress a 64-bit string to a smaller string.
#For example, the length of '10' * 32 is compressed to 325 digits, which is much
#larger than 64 digits. 
