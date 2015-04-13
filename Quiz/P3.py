import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

#pylab.hist(tVals, normed=1, histtype='stepfilled')

#PROBLEM 3-1
#The values in xVals are
#=> Uniformly distributed

#PROBLEM 3-2
#The values in tVals are
#=> Gaussian

#PROBLEM 3-3
#pylab.plot(xVals, yVals)
#=> Graph 4

#PROBLEM 3-4
#pylab.plot(xVals, zVals)
#=> Graph 5

#PROBLEM 3-5
#pylab.plot(sorted(xVals), yVals)
#=> Graph 2

#PROBLEM 3-6
#pylab.plot(xVals, sorted(yVals))
#=> Graph 3

#PROBLEM 3-7
#pylab.plot(sorted(xVals), sorted(yVals))
#=> Graph 1

pylab.show()