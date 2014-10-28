import random


class Drunk(object):
    def __init__(self, name):
        self.name = name
        self.path = []
    def getPath(self):
        return self.path
    def addToPath(self,location):
        self.path.append(location)
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
