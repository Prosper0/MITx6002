#L5 PROBLEM 1

import random

def getBallOfColor():
    """
        returns a random ball color of Red or Green
        Balls are not replaced once drawn.
    """
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for t in range(3):
        # For three trials, pick a ball
        ball = random.choice(balls)
        # Remove the chosen ball from the set of balls
        balls.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if getBallOfColor():
            numTrue += 1

    return "Probability of getting 3 balls of same color:" + str(float(numTrue)/float(numTrials))

print noReplacementSimulation(1)
print noReplacementSimulation(100)
print noReplacementSimulation(100000)