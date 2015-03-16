# Lesson 2, Problem 4
import random

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

        
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)


def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)
    
d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
