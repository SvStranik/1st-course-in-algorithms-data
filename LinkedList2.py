class Node:

    def __init__(self,v):
        self.value = v
        self.prev = None
        self.next = None 

class LinkedList2:  

    def __init__(self):
        self.head = None
        self.tail = None

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

    def delete(self, val, all=False):
        if self.head == None: return
        while self.head.value == val:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            self.head = self.head.next
            if all != True: return
        else:
            self.prev = None
        node = self.head
        while self.tail != node:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                node.next.next.prev = node
                node.next = node.next.next
                if all != True: return
                continue
            node = node.next

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
