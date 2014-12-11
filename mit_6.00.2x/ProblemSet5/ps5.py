# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

# Problem 2: Building up the Campus Map
#
"""
buildings anre nodes, paths are edges.

"""

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    
    print "Loading map from file..."

    g = WeightedDigraph()
    with open(mapFilename) as file:
        for line in file:
            (fro, to, total, outdoors) = tuple(line.split())
            src = Node(fro)
            dest = Node(to)
            total_dist = float(total)
            out_dist = float(outdoors)
            edge = WeightedEdge(src, dest, total_dist, out_dist)
            try:
                g.addNode(src)
            except Exception, e:
                pass
            try:
                g.addNode(dest)
            except Exception, e:
                pass
            try:
                g.addEdge(edge)
            except Exception, e:
                pass

    return g

def main():
    mitMap = load_map("mit_map.txt")
    print 'IsInstanceof Digraph?', isinstance(mitMap, Digraph)
    print 'IsInstanceof WeightedDigraph?', isinstance(mitMap, WeightedDigraph)
    #print 'Nodes', mitMap.nodes
    #print 'Edges', mitMap.edges
    bruteForceSearch(mitMap, 23, 34, 40, 20)

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    DFS(digraph, start, end)
    valid_paths = []
    #print 'All Paths: ', digraph.getPaths()
    for p in digraph.getPaths():
        if p[0] == start and p[-1] == end:
            valid_paths.append(p)
    #print 'Paths: ', valid_paths
    # Find appropriate path
    #return shortestPath(digraph, paths)
    #return shortestTotalPath(digraph, maxTotalDist, valid_paths)
    return shortestTotalPath(digraph, maxTotalDist, maxDistOutdoors, valid_paths)

def printPath(path):
    return path

def shortestPath(digraph, paths):
    shortest = digraph.edges
    for p in paths:
        if len(p) < len(shortest):
            shortest = p
    return shortest

def bothDists(graph, path):
    indoor = 0
    outdoor = 0
    for i in range(len(path)-1):
        dist, outdoor_dist = graph.getEdgeWeight(path[i], path[i+1])
        indoor += dist
        outdoor += outdoor_dist
        #print 'From ', path[i], 'to ', path[i+1] ,' costs', dist, ' ', outdoor_dist
    #print '** From ', path[0], 'to ', path[-1] ,' costs', indoor, ' ', outdoor
    return indoor, outdoor

def shortestTotalPath(digraph, maxDist, maxOutdoorDist, paths):
    path_by_dist = {}
    # This works because I don't care if I overwrite paths of equal distance
    for p in paths:
        #print '** Path = ', p, len(p)
        #print '** Paths = ', paths, len(paths)
        path_dist, path_outdoor_dist = bothDists(digraph,p)
        if path_dist > maxDist or path_outdoor_dist > maxOutdoorDist:
            continue
        total_dist = path_dist + path_outdoor_dist
        #print 'in: ', path_dist, ', out: ', path_outdoor_dist, ', total dist: ', total_dist, ', path = ', p
        path_by_dist[total_dist] = p
    return path_by_dist[min(path_by_dist)]

def DFS(graph, start, end, current_path = [], paths = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    current_path = current_path + [start]
    #print 'Current dfs path:', printPath(current_path)
    if start == end:
        return current_path
    for node in graph.childrenOf(Node(start)):
        if node.getName() not in current_path: #avoid cycles
            newPath = DFS(graph,node.getName(),end,current_path,paths)
            if newPath != None:
                #print 'newPath = ', newPath
                graph.addPath(newPath)
        else:
            pass

def DFSShortest(graph, start, end, current_path = [], maxTotal = 0 , maxOutdoor = 0):
    #print 'path: ', current_path
    curr_indoor, curr_outdoor = bothDists(graph, current_path)
    if (curr_indoor + curr_outdoor) > graph.getShortestPathLength():
        #print 'returning None'
        return None
    if curr_outdoor > maxOutdoor or (curr_indoor + curr_outdoor) > maxTotal:
        #print 'returning None'
        return None
    current_path = current_path + [start]
    #print 'Current dfs path:', printPath(current_path)
    if start == end:
        return current_path
    for node in graph.childrenOf(Node(start)):
        if node.getName() not in current_path: #avoid cycles
            newPath = DFSShortest(graph,node.getName(),end,current_path, maxTotal, maxOutdoor)
            if newPath != None:
                #print 'newPath = ', newPath
                curr_indoor, curr_outdoor = bothDists(graph, newPath)
                if (curr_indoor + curr_outdoor) < graph.getShortestPathLength():
                    #print 'newPath = ', newPath, ' with length ', (curr_indoor + curr_outdoor)
                    graph.setShortestPathLength(curr_indoor + curr_outdoor)
                graph.addPath(newPath)
        else:
            pass

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    DFSShortest(digraph, start, end, [], maxTotalDist, maxDistOutdoors)
    valid_paths = []
    #print 'All Paths: ', digraph.getPaths()
    for p in digraph.getPaths():
        if p[0] == start and p[-1] == end:
            valid_paths.append(p)
    #print 'Paths: ', valid_paths
    # Find appropriate path
    #return shortestPath(digraph, paths)
    #return shortestTotalPath(digraph, maxTotalDist, valid_paths)
    return shortestTotalPath(digraph, maxTotalDist, maxDistOutdoors, valid_paths)

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    mitMap = load_map("test_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges

    LARGE_DIST = 1000000

    #Test cases
    mitMap = load_map("mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    #print 'nodes', mitMap.nodes
    #print 'edges', mitMap.edges


    LARGE_DIST = 1000000

    #Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    print "Expected: ", expectedPath1
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Brute-force: ", brutePath1
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

##@#    test_map = load_map("test_map_1.txt")
##@#    br3 = bruteForceSearch(test_map, "1", "3", 100, 100)
##@#    ep3 = ['1', '2', '3']
##@#    print test_map 
##@#    print "Expected: ", ep3
##@#    print "Brute-force: ", br3

##@##     Test case 3
##@#    print "---------------"
##@#    print "Test case 3:"
##@#    print "Find the shortest-path from Building 2 to 9"
##@#    expectedPath3 = ['2', '3', '7', '9']
##@#    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
##@##     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
##@#    print "Expected: ", expectedPath3
##@#    print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
