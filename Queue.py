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
    
    def delete(self):
        if self.head == None: return None
        per = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return per
        
    def len(self):
        resultat = 0
        node = self.head
        while node is not None:
            resultat += 1
            node = node.next
        return resultat

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.add_in_tail(Node(item))

    def dequeue(self):
        return self.queue.delete()

    def size(self):
        return self.queue.len()