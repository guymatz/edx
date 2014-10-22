#!/usr/bin/env python


class Queue():
  
    def __init__(self):
        self.list = []

    def insert(self, thing):
        self.list.append(thing)

    def remove(self):
        if len(self.list) == 0:
          raise ValueError
        thing = self.list[0]
        self.list = self.list[1:]
        return thing

if __name__ == '__main__':
    queue = Queue()
    queue.insert(5)
    queue.insert(6)
    print queue.remove()
    queue.insert(7)
    print queue.remove()
    print queue.remove()
    print queue.remove()
