class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    def __init__(self, value, next):
        self.data = value
        self.next = next
        self.prev = None
    
    def __init__(self, value, prev, next):
        self.data = value
        self.next = next
        self.prev = prev

class SingleyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, elem):
        node = Node(elem, self.head)
        node.next = self.head
        self.head = node
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
        while (curr.next != None):
            curr = curr.next

        # Curr.next == None => end of list
        curr.next = Node(elem)
        size += 1

    def add(self, index, elem):
        curr = self.head
        if (0 > index or index >= self.size):
            return

        if index == 0:
            self.addFirst(elem)
            return

        for i in range(index-1):
            curr = curr.next
        
        # Curr == (index-1)th elements
        newNode = Node(elem, curr.next)
        curr.next = newNode
        self.size += 1

    def remove(self, index):
        if (0 > index or index >= self.size):
            return None
        elif (index == 0):
            self.removeFirst()

        curr = self.head
        prev = None
        for i in range(index-1):
            curr = curr.next

        # Curr = (index-1)th element
        prev = curr
        curr = curr.next # (index)th element
        data = curr.data
        prev.next = curr.next
        self.size -= 1
        return data

    def get(self, index):
        if (0 > index or index >= self.size):
            return None

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.data

    def assign(self, index, elem):
        if (0 > index or index >= self.size):
            return None

        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.data = elem

class DoubleyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, elem):
        node           = Node(elem, self.head)
        self.head.prev = node
        self.head      = node
        self.size      += 1

    def removeFirst(self, elem):
        if (self.head == None):
            return None
        else:
            headData       = self.head.data
            self.head      = self.head.next
            self.head.prev = None
            self.size      -= 1
            return headData

    def removeLast(self, elem):
        if (self.tail == None):
            return None
        else:
            tailData  = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return headData
    
    def size(self):
        return self.size

    def add(self, elem):
        if (self.size == 0):
            self.addFirst(elem)
            return

        curr = self.head
        while (curr.next != None):
            curr = curr.next

        # Curr.next == None => end of list
        node = Node(elem, None, curr)
        curr = curr.next
        size += 1

    def add(self, index, elem):
        curr = self.head
        if (0 > index or index >= self.size):
            return

        if index == 0:
            self.addFirst(elem)
            return
        elif index == self.size-1:
            self.add(elem)
            return

        for i in range(index-1):
            curr = curr.next
        
        # Curr == (index-1)th elements
        newNode = Node(elem, curr, curr.next)
        curr.next.prev = newNode
        curr.next = newNode
        self.size += 1

    def remove(self, index):
        if (0 > index or index >= self.size):
            return None
        elif (index == 0):
            self.removeFirst()
        elif (index == self.size - 1):
            self.removeLast()

        curr = self.head
        prev = None
        for i in range(index-1):
            curr = curr.next

        # Curr = (index-1)th element
        prev = curr
        curr = curr.next # (index)th element
        data = curr.data
        prev.next = curr.next
        prev.next.prev = prev
        self.size -= 1
        return data

    def get(self, index):
        if (0 > index or index >= self.size):
            return None

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.data

    def assign(self, index, elem):
        if (0 > index or index >= self.size):
            return None
            
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.data = elem
