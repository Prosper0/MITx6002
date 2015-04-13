# PROBLEM 6-1
#Suppose you have a six sided die, with sides number 1 through 6, and you roll it several times.
#As in the problems from Lecture 3, answer each question in reduced fraction form - eg 1/5 instead of 2/10.
#What is the probability that the first time you observe a 1 is on the second roll?
#=> 5/6 * (1 - 5/6) = 5/36

#PROBLEM 6-2
#What is the probability that the first time you observe a 1 is on the third roll?
#=> 5/6 * 5/6 * (1 - 5/6)

def probTest(limit):
    prob = 1.0
    n = 1
    while prob > limit:
        prob = (5.0/6.0)**(n-1)*1.0/6.0
        n += 1        
    return n-1
    
print probTest(25/216.0)