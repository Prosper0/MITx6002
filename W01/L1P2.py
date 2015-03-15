def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e
    
#lotsOfParameters1()
#lotsOfParameters1(1,2)
#lotsOfParameters1(a=5,b=1,c=4,d=2,3)


# OK
#lotsOfParameters1(1,e=5,d=4,c=3,b=2)
#lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)


def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

#lotsOfParameters2(1,c=2,3)
#lotsOfParameters2(1,e=20,b=3,a=10)


# OK
#lotsOfParameters2()
#lotsOfParameters2(1,2)
#lotsOfParameters2(1,c=2)
#lotsOfParameters2(1,e=20,b=3)


def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

#lotsOfParameters3()

# OK
#lotsOfParameters3(1,2)
#lotsOfParameters3(1,c=2)
#lotsOfParameters3(1,c=2,3)
#lotsOfParameters3(1,c=2,b=3)


