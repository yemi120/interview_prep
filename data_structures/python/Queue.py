from LinkedList import DoubleyLinkedList

class Queue(object):
    def __init__(self):
        self.list = DoubleyLinkedList()
        return
    
    def enqueue(self, elem):
        self.list.add(elem)

    def dequeue(self):
        return self.list.remove(0)

    def peek(self):
        return self.list.head.data

    def isEmpty(self):
        return self.list.head == None
