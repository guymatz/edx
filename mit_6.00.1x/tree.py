#!/usr/bin/env python

class Tree():

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def setLeft(self, left_node):
        self.left = left_node

    def setRight(self, right_node):
        self.left = right_node

    def dfSearch(self, value):
        search_list = [self]
        print("Searching %s" % self.value)
        for n in search_list:
            if self.value == value:
                print self.value
            else:
                if self.right:
                    search_list.insert(self.right.value)
                if self.left:
                    search_list.insert(self.left.value)
                search_list[0].dfSearch(value)


if __name__ == '__main__':
    t5 = Tree(5)
    t3 = Tree(3, t5)
    t2 = Tree(2, t3)
    t4 = Tree(4, t3)
    t3.setLeft(t2)
    t3.setRight(t4)
    t7 = Tree(7, t5)
    t6 = Tree(6, t7)
    t8 = Tree(4, t7)
    t7.setLeft(t6)
    t7.setRight(t8)

    t5.dfSearch(2)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
