class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value < v2.value: return -1
        elif v1.value == v2.value: return 0
        else: return 1

    def add(self, value):
        item = Node(value)
        if self.__ascending is True: status = 1
        else: status = -1
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            if self.compare(self.head,item) == status:
                self.head.prev = item
                item.next = self.head
                self.head = item
            else:
                node = self.head
                while node:
                    if self.compare(node,item) == status:
                        item.prev = node.prev
                        item.next = node
                        node.prev.next = item
                        node.prev = item
                        item.next = node
                        return
                    node = node.next
                item.prev = self.tail  
                self.tail.next = item
                self.tail = item


    def find(self, val):
        item = Node(val)
        node = self.head
        if self.__ascending is True: status = 1
        else: status = -1
        while node:
            per = self.compare(node,item)
            if per == 0: return node
            if status == per: return None
            node = node.next
        
        
    def delete(self, val,all=False):
        if self.head == None: return
        while self.head.value == val:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            self.head.next.prev = None
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


    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None


    def len(self):
        resultat = 0
        node = self.head
        while node:
            resultat += 1
            node = node.next
        return resultat 


    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.value.rstrip().lstrip() < v2.value.rstrip().lstrip(): return -1
        elif v1.value.rstrip().lstrip() == v2.value.rstrip().lstrip(): return 0
        else: return 1
        