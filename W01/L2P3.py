# Lesson 2, Problem 3A & B
import random

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randrange(10, 20, 2)

print "-- Detereministic ---"
print deterministicNumber()
print deterministicNumber()
print deterministicNumber()

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    random.seed(None)
    return random.randrange(10, 22, 2)

print "-- Stochastic ---"
print stochasticNumber()
print stochasticNumber()
print stochasticNumber()