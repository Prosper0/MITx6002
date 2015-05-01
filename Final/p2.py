#import pylab, string, numpy
from numpy import *

# PROBLEM 2-1
#a = 1.0
#b = 2.0
#c = 4.0
#yVals = []
#xVals = range(-20, 20)
#for x in xVals:
#    yVals.append(a*x**2 + b*x + c)
#yVals = 2*pylab.array(yVals)
#xVals = pylab.array(xVals)
#try:
#    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
#    print a, b, c, d
#except:
#    print 'fell to here'

# Problem 2-2

data_A = [0,1,2,3,4,5,6,7,8] # v=6.66666666667 m=4.0
data_B = [5,10,10,10,15] #     v=10.0          m=10.0
data_C = [0,1,2,4,6,8] #       v=7.91666666667 m=3.5
data_D = [6,7,11,12,13,15] #   v=10.2222222222 m=10.6666666667
data_E = [9,0,0,3,3,3,6,6] #   v=8.4375        m=3.75
#print "Data:" + str(data)
#print str(var(data))
#print str(mean(data))

all_data = [data_A,data_B,data_C,data_D,data_E]

# Problem 2-3

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

for dta in all_data:
    print "Data:" + str(dta)
    print "Possible_var=" + str(possible_variance(dta))