class Node:

    def __init__(self,v):
        self.value = v
        self.next = None
        self.prev = None
         
    
    def get_next(self,node):
        self.next = node
   
    def get_prev(self,node):
        self.prev = node
        
    def node_prev(self):
        return self.prev
        
    def node_next(self):
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
        noda2 = noda.node_prev()
        noda.get_prev(newNode)
        newNode.get_next(noda)
        noda2.get_next(newNode)
        newNode.get_prev(noda2)
        
    def delete(self, val):
        noda = self.head
        while noda:
            if noda.value == val:
                noda.node_prev().get_next(noda.node_next())
                noda.node_next().get_prev(noda.node_prev())
            noda = noda.node_next()