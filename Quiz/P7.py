import random, pylab

#found_Vals = {'black': 0, 'white': 0}
#
#prev_was_black = False
#
#for i in range(1000):
#    if random.random() > 0.5:
#        prev_was_black = True
#        found_Vals['black'] += 1
#    else:
#        prev_was_black = False
#        found_Vals['white'] += 1
#
##pylab.hist(found_Vals, bins=2, normed=1)
##pylab.show()
#
#print "White:" + str(found_Vals['black']) + " Black:" + str(found_Vals['white'])

found_Vals = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

first_run = True
prev_was_black = False
cnt_steps = 0

for i in range(1000):
    if prev_was_black and not first_run:
        cnt_steps += 1
    else:
        cnt_steps = 0
    
    if random.random() > 0.5:
        prev_was_black = True
        found_Vals[cnt_steps] += 1
    else:
        prev_was_black = False
        found_Vals[cnt_steps] += 1
        
    first_run = False

pylab.bar(range(len(found_Vals)), found_Vals.values(), align='center')
pylab.xticks(range(len(found_Vals)), found_Vals.keys())

pylab.show()

#pylab.hist(found_Vals, bins=2, normed=1)
#pylab.show()

#print str(found_Vals)