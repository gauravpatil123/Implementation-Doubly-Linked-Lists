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
        return self.num == 0

    # returns number of elements
    def size(self):
        return self.num

    # prepends element to the collection
    def addFirst(self, item):
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
        self.first = Node(None)
        self.last = Node(None)
        self.num = 0
        self.first.next = self.last
        self.last.prev = self.first

    # creates and return identical list
    def clone(self):
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

    # checks if the lsit has the specified element
    def contains(self, item):
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
        if (self.num == 0):
            raise Exception("List is empty")
        return self.first.next.item

    # returns element at a specified position
    def get(self, index):
        idx = 0
        current = self.first.next

        while (idx != index):
            current = current.next
            idx += 1

        item = current.item
        return item

    # returns first element
    def getFirst(self):
        if (self.num == 0):
            raise Exception("List is empty")
        return self.first.next.item

    # returns last element
    def getLast(self):
         if (self.num == 0):
             raise Exception("List is empty")
         return self.last.prev.item

    # returns the index of first occurence of specified element or -1 if no such element
    def indexOf(self, item):
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
        if (self.num == 0):
            raise Exception("List is empty")
        current = Node(None)
        current.next = self.first.next
        while (current.next != self.last):
            item = current.next.item
            current.next = current.next.next
            yield item

# tests
words = DoublyLinkedList()
print("Is the list empty : "+ str(words.isEmpty()))
print("LL size = " + str(words.size()))
words.addFirst("Ace")
words.addLast("King")
words.addLast("Queen")
words.addFirst("Two")
words.addFirst("One")
words.addLast("Jack")
print("LL size = "+str(words.size()))
print("Current List is : ")
for s in words.iterate():
    print(s)
words.removeFirst()
words.removeLast()
words.removeFirst()
words.removeFirst()
for s in words.iterate():
    print(s)
print("LL size = " + str(words.size()))
words.add(1, "Ace")
words.add(0, "Five")
for s in words.iterate():
    print(s)
print("LL size = "+str(words.size()))
newWords = words.clone()
for s in newWords.iterate():
    print(s)
newWords.clear()
#for s in newWords.iterate():
#    print(s)
print(str(words.contains("Ace")))
print(str(words.contains("Seven")))
print(str(words.element()))
for s in words.iterate():
    print(s)
print(str(words.get(3)))
print(str(words.get(2)))
print(str(words.getFirst()))
print(str(words.getLast()))
print(str(words.indexOf("Ace")))
print(str(words.indexOf("Eight")))

