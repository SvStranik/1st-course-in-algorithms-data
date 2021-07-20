class Node:

    def __init__(self,v):
        self.value = v
        self.prev = None
        self.next = None 

class DummyNode(Node):
    def __init__(self,v):
        super.__init__(v)

        
        
class LinkedList2:  

    def __init__(self):
        self.head = DummyNode("head")
        self.tail = DummyNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_in_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
        
        
    def delete(self, val):
        node = self.head
        while node:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next
    
    def print_all(self):
        node = self.head.next
        while node.next != None:
            print(node.value)
            node = node.next