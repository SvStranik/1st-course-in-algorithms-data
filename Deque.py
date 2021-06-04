class Node:


    def __init__(self,v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList:


    def __init__(self):
        self.head = None
        self.tail = None


    def add_in_tail(self,item): 
        if self.head is None:
            self.head = item
        else: 
            item.prev = self.tail
            self.tail.next = item 
        self.tail = item
        

    def add_in_head(self,item): 
        if self.head is None:
            self.tail = item
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item
        

    def delete_head(self):
        if self.head == None: return None
        per = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return per
    

    def delete_tail(self):
        if self.head == None: return None
        per = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return per
        

    def len(self):
        resultat = 0
        node = self.head
        while node is not None:
            resultat += 1
            node = node.next
        return resultat
        

class Deque:
    def __init__(self):
        self.deque = LinkedList()


    def addFront(self, item):
        self.deque.add_in_head(Node(item))

      
    def addTail(self, item):
        self.deque.add_in_tail(Node(item))
       

    def removeFront(self):
        return self.deque.delete_head()


    def removeTail(self):
        return self.deque.delete_tail()


    def size(self):
        return self.deque.len()
