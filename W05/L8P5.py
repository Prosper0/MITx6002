# L8 PROBLEM 5

def dToB(n, numDigits):
	"""requires: n is a natural number less then 2**numDigits
	returns a binary string of length numDigits representing the
	decimal number n."""
	assert type(n) == int and type(numDigits)==int and n >= 0 and n < 2**numDigits
	bStr = ''
	while n > 0:
		n = n//2
	while numDigits - len(bStr) > 0:
		bStr = '0' + bStr
	return bStr

def genPset(Items):
	"""Generate a list of lists representing the power set of items"""
	numSubsets = 2**len(Items)
	templates = []
	for i in range(numSubsets):
		templates.append(dtoB(i, len(Items)))
	pset = []
	for t in templates:
		elem = []
		for j in range(len(t)):
			if t[j] == '1':
				elem.append(Items[j])
		pset.append(elem)
	return pset

###############
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for result in powerset([1, 2, 3]):
    print(result)

results = list(powerset([1, 2, 3]))
print(results)

###
i = set([1, 2, 3])

def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield set(subset)

for i in powerset_generator(i):
    print i
