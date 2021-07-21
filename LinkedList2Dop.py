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
        node = self.tail
        node2 = node.get_prev()
        node.set_prev(newNode)
        newNode.set_next(node)
        node2.set_next(newNode)
        newNode.set_prev(node2)

    def delete(self, val, all = False):
        node = self.head.get_next()
        while node:
            if node.value == val:
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
                if all is False: return
            node = node.get_next()
    
    def find(self, val):
        node = self.head.get_next()
        while not isinstance(node,DummyNode):
            if node.value == val: return node
            node = node.get_next()
        return None 
    
    def find_all(self, val):
        node = self.head.get_next()
        resultat = []
        while not isinstance(node,DummyNode):
            if node.value == val: 
                resultat.append(node)
            node = node.get_next()
        return resultat 
        
    def clean(self):
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)
        
    def len(self):
        resultat = 0
        node =self.head.get_next()
        while not isinstance(node,DummyNode):
            resultat += 1
            node = node.next
        return resultat 
        
    def insert(self, afterNode, newNode):
        if isinstance(afterNode,Node):
            afterNode.get_next().set_prev(newNode)
            newNode.set_next(afterNode.get_next())
            afterNode.set_next(newNode)
            newNode.set_prev(afterNode)
        else:
            self.add_in_tail(newNode)

    def add_in_head(self, newNode):
        node = self.head
        node2 = node.get_next()
        node.set_next(newNode)
        newNode.set_prev(node)
        node2.set_prev(newNode)
        newNode.set_next(node2)
        
    def print_all(self):
        node = self.head.get_next()
        while not isinstance(node,DummyNode):
            print(node.value)
            node = node.get_next()
