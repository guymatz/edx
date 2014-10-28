from drunk import UsualDrunk, Drunk
from location import Location
from field import Field

import pylab
import time

def walk(f, d, numSteps):
  start = f.getLoc(d)
  for s in range(numSteps):
      f.moveDrunk(d)
  path = d.getPath()
  drawPath(numSteps, path)
  return(start.distFrom(f.getLoc(d)))


def simWalks(numSteps, numTrials):
  distances = []
  for t in range(numTrials):
      homer = UsualDrunk('Homer')
      origin = Location(0, 0)
      f = Field()
      f.addDrunk(homer, origin)
      distances.append(walk(f, homer, numSteps))
  return distances



#for numSteps in [10, 100, 1000, 10000]:
def drunkTest(numTrials = 5):
  for numSteps in [10, 100, 1000, 10000]:
      distances = simWalks(numSteps, numTrials)
      print 'Random walk of ' + str(numSteps) + ' steps'
      print ' Mean =', sum(distances)/len(distances)
      print ' Max =', max(distances), 'Min =', min(distances)

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
  now = str(time.time())
  pylab.savefig(now + '.jpg')

drunkTest()
