#!/usr/bin/env python
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

c = Coordinate(4,5)
d = Coordinate(4,5)
e = Coordinate(4,6)
if c == d:
  print("yes, c == d")
else:
  print("no, c != d")

if c == e:
  print("yes, c == e")
else:
  print("no, c != e")

if eval(repr(c)) == c:
  print("good")
else:
  print("bad")

print(repr(c))
