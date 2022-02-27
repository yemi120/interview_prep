from LinkedList import SingleyLinkedList

class Stack(object):
    def __init__(self):
        self.list = SingleyLinkedList()
        return
    
    def push(self, elem):
        self.list.add(elem, 0)
    
    def pop(self):
        return self.list.remove(0)

    def peek(self):
        return self.list.head.data

    def isEmpty(self):
        return self.list.head == None
