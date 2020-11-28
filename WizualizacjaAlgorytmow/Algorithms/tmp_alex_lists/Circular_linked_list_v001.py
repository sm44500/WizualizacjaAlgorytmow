class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Circular_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_back(self, element):
        if not self.length:
            self.head = Node(element)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Node(element, self.head)
        self.length += 1

    def push_front(self, element):
        if not self.length:
            self.head = Node(element)
            self.head.next = self.head
        else:
            current = Node(self.head.data, self.head.next)
            self.head = Node(element, current)
        self.length += 1

    def insert (self, position, element):
        pass

    def remove_element(self, element):
        current = self.head
        if current.data == element:
            self.head = current.next
        else:
            count = 0
            while (current.next.data != element):
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
        tmp = []
        current = self.head
        for i in range(self.length * 2):
            #tmp.append(current.data)
            print(current.data, end = " ")
            current = current.next
        print("\n")
        #return " ".join(tmp)

mylist = Circular_linked_list()
for i in range(9):
    mylist.push_front(i)
mylist.out()

