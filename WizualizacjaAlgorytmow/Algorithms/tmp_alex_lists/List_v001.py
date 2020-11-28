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
        pass

    def remove_element(self, element):
        current = self.head
        if current.data == element:
            self.head = current.next
        else:
            while current.next.data != element:
                if count == self.length:
                    break
                current = current.next
                count += 1
            current.next = current.next.next
        self.length -= 1

    def find_element(self, element):
        pass

    def clear(self):
        self.head = None
        self.length = 0

    def empty(self):
        return bool(length)

    def out(self):
        current = self.head
        for i in range(self.length):
            print(current.data, end = " ")
            current = current.next
        print("\n")

#mylist = List()
#for i in range(9):
#    mylist.push_front(i)
#mylist.out()
#mylist.remove_element(8)
#mylist.out()
