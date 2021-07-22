class Node:

    def __init__(self,v):
        self.value = v
        self.next = None
        self.prev = None
         
    def set_next(self,node):
        self.next = node
   
    def set_prev(self,node):
        self.prev = node
        
    def get_next(self):
        if isinstance(self.next,DummyTail):
            return None
        return self.next
        
    def get_prev(self):
        return self.prev
        
class DummyHead(Node):
    def __init__(self,v):
        super().__init__(v)
    
    def get_next(self):
        if not isinstance(self,Node):
            return self.head
        return self.next
    
        
class DummyTail(Node):
    def __init__(self,v):
        super().__init__(v)
    
    def get_prev(self):
        if not isinstance(self,Node):
            return self.tail
        return self.prev

class LinkedList2:  

    def __init__(self):
        self.head = DummyHead('Head')
        self.tail = DummyTail('Tail')
        self.tail.prev = self.head
        self.head.next = self.tail
        
    def add_in_tail(self, newNode):
        node = DummyTail.get_prev(self)
        node2 = node.get_prev()
        node.set_prev(newNode)
        newNode.set_next(node)
        node2.set_next(newNode)
        newNode.set_prev(node2)
    
    def add_in_head(self, newNode):
        node = DummyHead.get_next(self)
        node2 = node.get_next()
        node.set_next(newNode)
        newNode.set_prev(node)
        node2.set_prev(newNode)
        newNode.set_next(node2)
        
    def delete(self, val, all = True):
        node = DummyHead.get_next(self).get_next()
        while node:
            if node.value == val:
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
                if all is False: return
            node = node.get_next()
         
    def find(self, val):
        node = DummyHead.get_next(self).get_next()
        while node:
            if node.value == val: return node
            node = node.get_next()
        return None 
    
    def find_all(self, val):
        node = DummyHead.get_next(self).get_next()
        resultat = []
        while node:
            if node.value == val: 
                resultat.append(node)
            node = node.get_next()
        return resultat 
        
    def clean(self):
        DummyHead.get_next(self).set_next(DummyTail.get_prev(self))
        DummyTail.get_prev(self).set_prev(DummyHead.get_next(self))
        
    def len(self):
        resultat = 0
        node = DummyHead.get_next(self).get_next()
        while node:
            resultat += 1
            node = node.get_next()
        return resultat 
        
    def insert(self, afterNode, newNode):
        if isinstance(afterNode,Node):
            afterNode.get_next().set_prev(newNode)
            newNode.set_next(afterNode.get_next())
            afterNode.set_next(newNode)
            newNode.set_prev(afterNode)
        else:
            self.add_in_tail(newNode)
            
    def printNode(self):
        node = DummyHead.get_next(self).get_next()
        while node:
            print(node.value)
            node = node.get_next()