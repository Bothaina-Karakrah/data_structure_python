class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        return

class LinkedList:

    def __init__(self):
        self.head = None
        self.len = 0
        return

    def __insert__(self, data):
        new_node = Node(data)
        curr = self.head

        ## if list is empty
        if curr == None:
            self.head = new_node

        ## add it before head
        elif curr.data >= data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            ##find its place in the list
            while(curr.next != None and curr.next.data < data):
                curr = curr.next

            new_node.next = curr.next
            new_node.prev = curr

            if curr.next != None:
                curr.next.prev = new_node
            curr.next = new_node

        self.len += 1
        return

    def __delete__(self, data):
        curr = self.head

        ##delete the head
        if self.head.data == data:
            self.head = self.head.next
            self.len -= 1
            return

        ##find it in the list
        while (curr != None and curr.data < data):
            curr = curr.next

        if curr!= None and curr.data == data:
            curr.prev.next = curr.next
            if curr.next != None:
                curr.next.prev = curr.prev
            self.len -= 1

        return

    def getLen(self):
        return self.len

    def __get__(self, position):
        if position > self.len:
            return None

        i = 1
        curr = self.head
        while i < position:
            curr = curr.next
            i += 1

        return curr.data

    def __set__(self, position, value):
        if position > self.len:
            return

        i = 1
        curr = self.head
        while i < position:
            curr = curr.next
            i += 1

        curr.data = value
        return

    def clearFromTo(self, startIndex, stopIndex):
        if startIndex < 0:
            startIndex = 0

        if stopIndex > self.len:
            return

        i = 1
        currStart = self.head

        while i < startIndex:
            currStart = currStart.next
            i += 1

        currStop = currStart
        while i < stopIndex:
            currStop = currStop.next
            i += 1

        if currStart.prev == None:
            self.head = currStop.next

        else:
            currStart.prev.next = currStop.next

        if currStop.next == None:
            self.head = None

        else:
            currStop.next.prev = currStart.prev

        self.len = self.len - (stopIndex - startIndex + 1)
        return

    def clear(self):
        self.clearFromTo(1, self.len)
        return

    def setZero(self, startIndex, stopIndex):
        if startIndex < 0:
            startIndex = 0

        if stopIndex > self.len:
            return

        i = 1
        curr = self.head

        while i < startIndex:
            curr = curr.next
            i += 1

        while i < stopIndex + 1:
            curr.data = 0
            curr = curr.next
            i += 1

        return

    def setAllZero(self):
        self.setZero(1, self.len)
        return

    ## print the list
    def print(self):
        curr = self.head

        while(curr != None):
            print(curr.data)
            curr = curr.next

        print(f"the len is: {self.len}")
        return


##test it
my_list = LinkedList()
my_list.__insert__('a')
my_list.__insert__('k')
my_list.__insert__('c')
my_list.__insert__('d')
my_list.__insert__('f')
my_list.print()
my_list.setAllZero()
my_list.print()
