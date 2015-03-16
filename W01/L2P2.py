# Lesson 2, Problem 2
import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    return random.randrange(0, 100, 2)
    
print genEven()
print genEven()
print genEven()
print genEven()