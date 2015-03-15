# Lecture 1, Problem 3 & 4

import pylab
import numpy as np

PATH_TO_TEMPS_FILE = r'F:\Dev\Python\MITx6002\W01\julyTemps.txt'

def loadTemps():
    inFile = open(PATH_TO_TEMPS_FILE, 'r', 0)
    high_temps = []
    low_temps = []
    
    for line in inFile:
        fields = line.split(" ")
        
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high_temps.append(int(fields[1]))
            low_temps.append(int(fields[2]))

    return (high_temps, low_temps)
    
def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.plot(lowTemps)
    pylab.plot(highTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
(lowTemps, highTemps) = loadTemps()    
producePlot(lowTemps, highTemps)