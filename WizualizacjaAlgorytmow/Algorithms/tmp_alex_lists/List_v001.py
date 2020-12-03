#from Algorithms.BasicAlgorithm import BasicAlgorithm
#from Snapshot import Snapshot


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_back(self, element):
        if not self.length:
            self.head = Node(element)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(element)
        self.length += 1

    def push_front(self, element):
        if not self.length:
            self.head = Node(element)
        else:
            current = Node(self.head.data, self.head.next)
            self.head = Node(element, current)
        self.length += 1

    def insert(self, position, element):
        if position <= 0:
            self.push_front(element)
        elif position >= self.length - 1:
            self.push_back(element)
        else:
            current = self.head
            pos = 0
            while pos != position:
                current = current.next
            tmp = current.next
            current.next = Node(element, tmp)
        self.length += 1

    def remove(self, element):
        if not self.empty():
            current = self.head
            previous = None
            
            while current.next.data != element:
                previous = current
                current = current.next
                if current == None:
                    break
                    

            print(current.next.data)
            if current.data == element:
                current.next = current.next.next
                
            self.length -= 1
        else:
            return "The list is empty"

    def find(self, element):
        current = self.head
        index = 0
        while current.next != None:
            if (current.data == element):
                return [index, current]
            current = current.next
            index += 1
        return "There's no matching element in the list"

    def clear(self):
        self.head = None
        self.length = 0

    def empty(self):
        return bool(not self.length)

    def out(self):
        current = self.head
        for i in range(self.length):
            print(current.data, end = " ")
            current = current.next
        print("\n")

mylist = List()
for i in range(9):
    mylist.push_front(i)
mylist.out()
mylist.push_back(10)
mylist.out()
mylist.remove(8)
mylist.out()
mylist.remove(10)
mylist.out()


mylist.remove(10)
mylist.out()






