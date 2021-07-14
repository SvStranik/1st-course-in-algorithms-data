class Node:

    def __init__(self,v):
        self.value = v
        self.prev = None
        self.next = None 

class DummyNode:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
    
class LinkedList2(DummyNode):  

    def __init__(self):
        super().__init__()
        
    def add_in_tail(self, item):
        head = self.head
        tail = self.tail
        if head.next == None:
            head.next = item
            item.prev = head
            tail.prev = item
        else:
            item.prev = tail.prev
            tail.prev.next = item
            tail.prev = item
        item.next = tail
        
        
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