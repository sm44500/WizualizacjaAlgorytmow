from List_v001 import Node, List

class Double_linked_list(List):
    def __init__(self):
        super().__init__()
        self.tail = None
    
    def push_back(self, element):
        if self.empty():
            self.head = Node(element, self.tail, None)
            self.tail = self.head
        else:
            tmp = self.tail
            self.tail.next = Node(element, None, tmp)
            self.tail = self.tail.next
        self.length += 1
        #node = super().push_back(element)
        pass

    def push_front(self, element):
        #return super().push_front(element)
        if self.empty():
            self.head = Node(element, self.tail, None)
            self.tail = self.head
        else:
            tmp = self.head()
            self.head.previous = Node(element, tmp, None)
            self.head = self.head.previous
        self.length += 1
        pass

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
        pass

    def remove(self, element):
        if not self.empty():
            if self.head.data == element:
                self.head = self.head.next
                self.head.previous = None
                self.length -= 1
            elif self.tail.data == element:
                self.tail = self.tail.previous
                self.tail.next = None
                self.length -= 1
            else:
                current = self.head
                while current.data != element and current.next != None:
                    current = current.next
                if current.data == element:
                    #tmp = current
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.length -= 1
        else:
            return "The list is already empty"



