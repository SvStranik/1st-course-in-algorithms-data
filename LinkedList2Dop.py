class Node:

    def __init__(self,v):
        self.value = v
        self.next = None
        self.prev = None
         
    def set_next(self,node):
        self.next = node
   
    def set_prev(self,node):
        self.prev = node
        
    def get_prev(self):
        return self.prev
        
    def get_next(self):
        return self.next
        
class DummyNode(Node):
    def __init__(self,v):
        super().__init__(v)

class LinkedList2:  

    def __init__(self):
        self.head = DummyNode('Head')
        self.tail = DummyNode('Tail')
        self.tail.prev = self.head
        self.head.next = self.tail
   
    def add_in_tail(self, newNode):
        noda = self.tail
        noda2 = noda.get_prev()
        noda.set_prev(newNode)
        newNode.set_next(noda)
        noda2.set_next(newNode)
        newNode.set_prev(noda2)
        
    def delete(self, val):
        noda = self.head
        while noda:
            if noda.value == val:
                noda.get_prev().set_next(noda.get_next())
                noda.get_next().set_prev(noda.get_prev())
            noda = noda.get_next()