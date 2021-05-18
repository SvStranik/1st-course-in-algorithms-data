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
            print(node.value)
            node = node.next
    
    def find(self,val):
        node = self.head
        while node is not None:
            if node.value == val: return node
            node = node.next
        return None
    
    def delete(self,val,all=False):
        node = self.head
        while node.value == val:
            self.head = node.next
            if node.next == None:
                self.head = None
                self.tail = None
                return
            if all == False:return
            node = node.next
        while node.next is not None:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                else:
                    node.next = node.next.next
                    if all == False:
                        return
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
        node = self.head
        per = False  
        while per is not True:
            if node == afterNode:
                if node.next == None:
                    newNode.next = self.head
                    self.head = newNode
                else:    
                    newNode.next = node.next
                    node.next = newNode
                per = True
            node = node.next
            
