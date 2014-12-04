class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        
    def getWeight(self):
        return self.weight

    def __str__(self):
        return "%s->%s (%i)   " % (self.src.getName(), self.dest.getName(), self.weight)
