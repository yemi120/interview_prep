class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    def __init__(self, value, next):
        self.data = value
        self.next = next
        self.prev = None
    
    def __init__(self, value, next, prev):
        self.data = value
        self.next = next
        self.prev = prev

class SingleyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, elem):
        self.head = Node(elem, self.head)
        self.size += 1

    def removeFirst(self, elem):
        if (self.head == None):
            return None
        else:
            headData  = self.head.data
            self.head = self.head.next
            self.size -= 1
            return headData
    
    def size(self):
        return self.size

    def add(self, elem):
        if (self.size == 0):
            self.addFirst(elem)
            return

        curr = self.head
        while (curr != None):
            if (curr.next == None):
                curr.next = Node(elem)
                curr = curr.next
                size += 1
                return

    def add(self, index, elem):
        curr = self.head
        if (0 > index or index >= self.size):
            return
        if index == 0:
            self.addFirst(elem)
            return

        for i in range(index):
            if (i == index-1):
                newNode = Node(elem)
                newNode.next = curr.next
                curr.next = newNode
                self.size += 1
                return
            curr = curr.next

    def remove(self, index):
        if (0 > index or index >= self.size):
            return None
        elif (index == 0):
            self.removeFirst()

        curr = self.head
        prev = None
        for i in range(index+1):
            if (i == index-1):
                prev = curr
            elif (i == index):
                data = curr.data
                prev.next = curr.next
                self.size -= 1
                return data
            curr = curr.next
    def get(self, index):
        if (0 > index or index >= self.size):
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.data

    def set(self, index, elem):
        if (0 > index or index >= self.size):
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.data = elem
