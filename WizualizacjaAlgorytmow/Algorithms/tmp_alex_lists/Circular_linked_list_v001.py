from List_v001 import Node, List


class Circular_linked_list(List):
    def __init__(self):
        super().__init__()

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
            current = self.head
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            self.head = Node(element, current)
            tmp.next = self.head
        self.length += 1

    def clear(self):
        self.head = None
        self.length = 0

mylist = Circular_linked_list()
for i in range(9):
    mylist.push_front(i)
for i in range(20, 29):
    mylist.push_back(i)
mylist.out()


