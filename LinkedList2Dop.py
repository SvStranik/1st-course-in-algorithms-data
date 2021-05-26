class Linked:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self,val, all = False):
        if self.head == None: return
        self.add_in_head(Node("HEAD"))
        self.add_in_tail(Node("TAIL"))
        node = self.head
        while node.next:
            node = node.next
            if node.value ==val:
                node.next.prev = node.prev
                node.prev.next = node.next
                if all == False: break
        if self.head.next == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.tail = self.tail.prev
            self.tail.next = None            
    
class Node:

    def __init__(self,v):
        self.value = v
        self.prev = None
        self.next = None 

class LinkedList2(Linked): 
    
    def __init__(self):
        super().__init__()
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node:
            if node.value == val: return node
            node = node.next
        return None 

    def find_all(self, val):
        node = self.head
        resultat = []
        while node:
            if node.value == val: 
                resultat.append(node)
            node = node.next
        return resultat 

    def clean(self):
        self.head = None
        self.tail = None 

    def len(self):
        resultat = 0
        node = self.head
        while node:
            resultat += 1
            node = node.next
        return resultat 

    def insert(self, afterNode, newNode):
        node = self.head
        if node == None:
            self.head = newNode
            self.tail = newNode
            return
        while node:
            if node == afterNode:
                if node.next == None:
                    self.tail = newNode
                    newNode.prev = node
                else:
                    node.next.prev = newNode
                    newNode.next = node.next
                    newNode.prev = node
                node.next = newNode
                return
            if node.next == None and node != afterNode:
                node.next = newNode
                newNode.prev = node
                self.tail = newNode
                return
            node = node.next

    def add_in_head(self, newNode):
        node = self.head
        if node == None:
            self.tail = newNode
        else:
            node.prev = newNode
            newNode.next = node
        self.head = newNode

s_list1 = LinkedList2()
s_list1.add_in_tail(Node(2))
s_list1.add_in_tail(Node(1))
s_list1.add_in_tail(Node(2))
s_list1.delete(2)