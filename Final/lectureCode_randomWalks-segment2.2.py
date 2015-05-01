import pylab

class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'





class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        drunk.addToPath(currentLocation)
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random


class Drunk(object):
    def __init__(self, name):
        self.name = name
        self.path = []
    def __str__(self):
        return 'This drunk is named ' + self.name
    def getPath(self):
        return self.path
    def addToPath(self,location):
        self.path.append(location)
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0),(1.0,0.0),(1.0,1.0)]
            #[(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
  start = f.getLoc(d)
  for s in range(numSteps):
      f.moveDrunk(d)
  path = d.getPath()
  drawPath(numSteps, path)
  return(start.distFrom(f.getLoc(d)))


def drawPath(numSteps, path):
  pylab.figure(1)
  pylab.title('Path of Drunk - %i steps' % numSteps)
  pylab.xlabel('East/West')
  pylab.ylabel('North/South')
  xrange = [ x.getX() for x in path ]
  yrange = [ x.getY() for x in path ]
  #print xrange
  #print yrange
  pylab.plot(xrange,yrange)
  pylab.show()
  
homer = UsualDrunk('Homer')
f = Field()
origin = Location(0, 0)
f.addDrunk(homer, origin)

walk(f, homer, 500)