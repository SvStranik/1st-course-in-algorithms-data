class Node:

    def __init__(self,v):
        self.value = v
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self,item): 
        if self.head is None: self.head = item
        else: self.tail.next = item
        self.tail = item
        
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            node = node.next
    
    def find(self,val):
        node = self.head
        while node is not None:
            if node.value == val: return node
            node = node.next
        return None
    
    def delete(self,val,all=False):
        if self.head == None: return
        while self.head.value == val:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            self.head = self.head.next
            if all != True:return
        node = self.head
        while self.tail != node:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                node.next = node.next.next
                if all != True:return
                continue
            node = node.next
    
    def clean(self):
        self.head = None
        self.tail = None
        
    def find_all(self,val):
        resultat = []
        node = self.head
        while node is not None:
            if node.value == val: resultat.append(node)
            node = node.next
        return resultat
        
    def len(self):
        resultat = 0
        node = self.head
        while node is not None:
            resultat += 1
            node = node.next
        return resultat
    
    def insert(self,afterNode, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        node = self.head
        per = False  
        while per is not True:
            if node == afterNode:  
                newNode.next = node.next
                node.next = newNode
                if node.next.next == None:
                    self.tail = newNode
                per = True
            if node.next == None and node != afterNode:
                newNode.next = self.head
                self.head = newNode
                return
            node = node.next