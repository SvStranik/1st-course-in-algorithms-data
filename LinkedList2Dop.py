class Node:

    def __init__(self,v):
        self.value = v
        self.prev = None
        self.next = None 

class DummyNode:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
    
class LinkedList2(DummyNode):  

    def __init__(self):
        super().__init__()
        
    def add_in_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
        
    def delete(self, val, all=False):
        head = self.head
        tail = self.tail
        while head != tail:
            if head.value == val:
                head.prev.next = head.next
                head.next.prev = head.prev
            head = head.next
    
    def print_all(self):
        node = self.head.next
        while node.next != None:
            print(node.value)
            node = node.next