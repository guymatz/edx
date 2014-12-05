from graph import WeightedDigraph, WeightedEdge, Node
#
##import unittest
##
##class TestGraphFunctions(unittest.TestCase):
##
##    def setUp(self):
#g = WeightedDigraph()
##self.assertTrue(g)
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#g.addNode(na)
#g.addNode(nb)
#g.addNode(nc)
#e1 = WeightedEdge(na, nb, 15, 10)
#print e1, 'a->b (15, 10)'
#print e1.getTotalDistance(), 15
#
#print e1.getOutdoorDistance(), 10
#
#e2 = WeightedEdge(na, nc, 14, 6)
#e3 = WeightedEdge(nb, nc, 3, 1)
#print e2, 'a->c (14, 6)'
#print e3, 'b->c (3, 1)'
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g
#print 'a->b (15.0, 10.0)', 'a->c (14.0, 6.0)','b->c (3.0, 1.0)'
#
g = WeightedDigraph()
nx = Node('x')
ny = Node('y')
nz = Node('z')
e1 = WeightedEdge(nx, ny, 18, 8)
e2 = WeightedEdge(ny, nz, 20, 1)
e3 = WeightedEdge(nz, nx, 7, 6)
g = WeightedDigraph()
g.addNode(nx)
g.addNode(ny)
g.addNode(nz)
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print g
