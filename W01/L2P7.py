#L2 PROBLEM 7

import random

random.seed(9001)
print random.randint(1, 10)
#1
print random.randint(1, 10)
#3
print random.randint(1, 10)
#6
print random.randint(1, 10)
#6
print random.randint(1, 10)
#7

print "---"
random.seed(9001)
for i in xrange(random.randint(1, 10)):
    print random.randint(1, 10)
#8
#9
#7
#6
#8
#10

print "---"
random.seed(9001)
d = random.randint(1, 10)
for i in xrange(random.randint(1, 10)):
    print d


print "---"
random.seed(9001)
d = random.randint(1, 10)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print d
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print random.randint(1, 10)
