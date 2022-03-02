class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.leftTree = None
        self.rightTree = None

    def getData(self):
        return self.data

    def getLeft(self):
        return self.leftTree

    def getRight(self):
        return self.rightTree

    def setData(self, data):
        self.data = data
    
    def setLeft(self, left):
        self.leftTree = left

    def setRight(self, right):
        self.rightTree = right

    def isLeafNode(self):
        return ((self.getData() != None) and (self.getLeft() == None) and
                (self.getRight() == None))

    def size(self):
        if (self.isLeafNode()):
            return 1
        return 1 + self.getLeft().size() + self.getRight().size()

    def min(self):
        if (self.isLeafNode()):
            return self.getData()
        elif (self.getRight() == None) :
            return min(self.getData(), self.getLeft().min())
        elif (self.getLeft() == None):
            return min(self.getData(), self.getRight().min())
        else:
            return min(self.getData(),
                       min(self.getLeft().min(), self.getRight().min()))
                    
    def max(self):
        if (self.isLeafNode()):
            return self.getData()
        elif (self.getRight() == None) :
            return max(self.getData(), self.getLeft().max())
        elif (self.getLeft() == None):
            return max(self.getData(), self.getRight().max())
        else:
            return max(self.getData(),
                       max(self.getLeft().max(), self.getRight().max()))

    def isBST(self):
        if (self.isLeafNode()):
            return True
        return ((self.getData() > self.getLeft().max()) and
                (self.getData() < self.getRight().min()))

    def contains(self, elem):
        res = False
        if (self.getData == elem):
            return True
        if ((not res) and (self.getLeft() != None)):
            res = self.getLeft().contains(elem)
        if ((not res) and (self.getRight() != None)):
            res = self.getRight().contains(elem)
        return res

    def pluckMaxNode(self):
        if (self.getRight() == None):
            return self
        else:
            max = self.getRight().getMaxNode()
            if (max.getData() == self.getRight().getData()):
                self.setRight = None
            return max

    def BSTRemove(self, elem):
        if (self == None):
            return

        if (self.getData() == elem):
            if (self.getLeft() == None):
                right = self.getLeft().getMaxNode()
                self.setData(right.getData())
                self.setLeft(right.getLeft())
                self.setRight(right.getRight())
            else:
                pred = self.getLeft().pluckMaxNode()
                self.setData(pred.getData())
                self.setLeft(pred.getLeft())
                self.setRight(pred.getRight())

        elif (self.getData() > elem):
            left = self.getLeft()
            self.setLeft(left.BSTRemove(elem))
            return

        elif (self.getData() < elem):
            right = self.getRight()
            self.setRight(right.BSTRemove(elem))
        



        
        
