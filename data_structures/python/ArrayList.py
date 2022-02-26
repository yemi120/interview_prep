class ArrayList(object):

    def __init__(self):
        self.list     = [None, None]
        self.capacity = 2
        self.size     = 0

    def __init__(self, list):
        n = len(list)
        self.list     = [None]*(n + n/2)
        self.capacity = (n + n/2)
        self.size     = n

    def __repr__(self):
        print(self.list)

    def grow(self, index):
        newList = [None]*(self.capacity + (self.capacity / 2))
        passedIndex = 0

        for i in range(self.size + 1):
            # At index where growth is set to occur.
            if (i == index):
                passedIndex = 1
                continue

            newList[i] = self.list[i + passedIndex]

        self.list = newList
        self.capacity += self.capacity / 2  

    def shrink(self):
        newList = [None]*((self.capacity / 2))
        for i in range(self.size):
            newList[i] = self.list[i]
        self.list = newList
        self.capacity = self.capacity / 2  

    # Appends element at the end of the ArrayList, returns true
    def add(self, element):
        return self.add(self.size, element)

    # Inserts element at position index within the ArrayList
    def add(self, index, element):
        if (0 > index or index >= self.size):
            return

        # The array has reached capacity and needs to grow by 50%
        if (self.size == self.capacity):
            self.grow(self.size)

        self[self.size] = element   
        self.size += 1 
        return True
    
    def clear(self):
        self.__init__()

    def contains(self, element):
        for i in range(self.size):
            if (element == self.list[i]):
                return True
        return False

    def get(self, index):
        if (0 > index or index >= self.size):
            return None
        return self.list[index]

    def indexOf(self, element):
        for i in range(self.size):
            if (element == self.list[i]):
                return i
        return -1

    def isEmpty(self):
        return 0 == self.size
    
    def remove(self, index):
        if (0 > index or index >= self.size):
            return None

        removedElement = self.list[index]
        for i in range(index, self.size):
            self.list[i] = self.list[i+1]

        self.size -= 1
        if (self.size < self.capacity/4):
            self.shrink()

        return removedElement

    def remove(self, element):
        index = self.indexOf(element)

        if index == -1:
            return False

        self.remove(index)
        return True

    def assign(self, index, element):
        if (0 > index or index >= self.size):
            return None

        replacedElement = self.list[index]
        self.list[index] = element
        return replacedElement

    def size(self):
        return self.sizeSS