# L4 PROBLEM 3

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n = len(L)
    if (n == 0):
        return float('NaN')
    X = []
    for s in L:
        X.append(len(s))

    return stdDev(X)
    
# using a separate function for std dev from lecture video
def stdDev(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

#Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
print stdDevOfLengths(['a', 'z', 'p'])

#Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], 
#stdDevOfLengths(L) should return 1.8708.
print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])