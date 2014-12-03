import knapsack

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which item(s) are in each bag.
    """
    N = len(items)
    print("There are %i items, and %i combos" % (N, 3**N))
    # enumerate the 2**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            a = i / (3**j)
            b = a % 3
            #print("i = %i,j = %i, a = %i, b = %i" %(i,j, a, b))
            #print("%i %i" %(b, c))
            # test bit jth of integer i
            if b == 0:
                bag1.append(items[j])
            elif b == 1:
                bag2.append(items[j])
        yield (bag1, bag2)
        #print("-------------------------")

items = knapsack.buildItems()
items = ['a','b','c']
#print [ x.getName() for x in items ]
combos = yieldAllCombos(items)
for b1, b2 in combos:
    pass
    for i in b1:
        print i,
    print '----',
    for i in b2:
        print i,
    print
    #raw_input("Press Enter . . ."        )
