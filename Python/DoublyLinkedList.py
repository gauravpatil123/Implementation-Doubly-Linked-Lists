class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.num = 0
        self.first.next = self.last
        self.last.prev = self.first

    # true if list is empty else false
    def isEmpty(self):
        """
        return True if the LL is empty else returns False
        """
        return self.num == 0

    # returns number of elements
    def size(self):
        """
        return the integer size of the list
        """
        return self.num

    # prepends element to the collection
    def addFirst(self, item):
        """
        Input: item
        Action: adds item to first position (0 index) of the list
        """
        if (item == None): 
            raise Exception("Illegal argument")

        newNode = Node(item)
        newNode.next = self.first.next
        newNode.prev = self.first
        self.first.next.prev = newNode
        self.first.next = newNode
        self.num += 1

    # appends element to the collection
    def addLast(self, item):
        """
        Input: item
        Action: adds item to the last position of the list
        """
        if (item == None):
            raise Exception("Illegal argument")

        newNode = Node(item)
        newNode.next = self.last
        newNode.prev = self.last.prev
        self.last.prev.next = newNode
        self.last.prev = newNode
        self.num += 1

    # Inserts element at specified position
    def add(self, index, item):
        """
        Inputs: an integer index, item
        Action: adds the item to the specified index in the list if the
                index in not out of bounds
        """
        if (index >= self.num or index < 0):
            raise Exception("Index out of bounds")
        if (item == None):
            raise Exception("Illegal input element")

        idx = 0
        current = Node(item)
        current.next = self.first.next
        
        while (idx != index):
            current.next = current.next.next
            idx += 1
        
        current.prev = current.next.prev
        current.prev.next.prev = current
        current.prev.next = current
        self.num += 1

    # removes first element of the list
    def removeFirst(self):
        """
        removes and returns the first element of the list (index = 0)
        """
        if (self.num == 0):
            raise Exception("List is empty")

        delNode = self.first.next
        out = delNode.item
        self.first.next = delNode.next
        self.first.next.prev = self.first
        self.num -= 1
        return out

    # removes last element of the list
    def removeLast(self):
        """
        removes and return the last element of the list
        """
        if (self.num == 0):
            raise Exception("List is empty")

        delNode = self.last.prev
        out = delNode.item
        self.last.prev = delNode.prev
        self.last.prev.next = self.last
        self.num -= 1
        return out

    # clears all elements of list
    def clear(self):
        """
        clears all the elements from the list
        """
        self.first = Node(None)
        self.last = Node(None)
        self.num = 0
        self.first.next = self.last
        self.last.prev = self.first

    # creates and return identical list
    def clone(self):
        """
        creates and returns a new identical linked list
        """
        newLL = DoublyLinkedList()
        count = 0
        current = Node(None)
        current.next = self.first.next

        while (count != self.num):
            item = current.next.item
            newLL.addLast(item)
            current.next = current.next.next
            count += 1

        return newLL

    # checks if the list has the specified element
    def contains(self, item):
        """
        Input: item
        Output: returns True if the Linked list has the input item
                else returns False
        """
        if (item == None):
            raise Exception("Illegal argument")

        current = self.first
        idx = 0

        while (idx != self.num):
            current = current.next
            element = current.item
            idx += 1
            if (element == item):
                return True

        return False
    
    # returns first element of the list without removing it
    def element(self):
        """
        return the first element of the list (index = 0)
        """
        if (self.num == 0):
            raise Exception("List is empty")
        return self.first.next.item

    # returns element at a specified position
    def get(self, index):
        """
        Input: an integer index
        Output: return the item fromt he list at the input index
                if the index is not out of bounds
        """
        if (index >= self.num):
            raise Exception("index out of bounds")

        idx = 0
        current = self.first.next

        while (idx != index):
            current = current.next
            idx += 1

        item = current.item
        return item

    # returns first element
    def getFirst(self):
        """
        returns the first element of list without mutation (index = 0)
        """
        if (self.num == 0):
            raise Exception("List is empty")
        return self.first.next.item

    # returns last element
    def getLast(self):
        """
        returns the last element of the list without mutation
        """
         if (self.num == 0):
             raise Exception("List is empty")
         return self.last.prev.item

    # returns the index of first occurence of specified element or -1 if no such element
    def indexOf(self, item):
        """
        Input: item
        Output: returns the index of the first occurence of the input item or
                -1 if no such item is present in the list
        """
        if (self.num == 0):
            return -1
        idx = 0
        current = self.first.next

        while (idx != self.num):
            currItem = current.item
            if (currItem == item):
                return idx
            current = current.next
            idx += 1

        return -1

    # iterates the list
    def iterate(self):
        """
        yields elements of the list according to index order
        """
        if (self.num == 0):
            raise Exception("List is empty")
        current = Node(None)
        current.next = self.first.next
        while (current.next != self.last):
            item = current.next.item
            current.next = current.next.next
            yield item

    # returns a python list
    def toList(self):
        """
        return a python list identical to the linked list
        """
        if (self.num == 0):
            raise Exception("List is empty")
        out = []
        for elem in self.iterate():
            out.append(elem)
        return out