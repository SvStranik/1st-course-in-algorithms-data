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
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

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

        # автоматическая вставка value 
        # в нужную позицию

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
        
        
    def delete(self, val):
        pass # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_value(self): # УДАЛИТЬ ФУНКЦИЮ
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.value.rstrip().lstrip() < v2.value.rstrip().lstrip(): return -1
        elif v1.value.rstrip().lstrip() == v2.value.rstrip().lstrip(): return 0
        else: return 1
        # переопределённая версия для строк
 

#Or = OrderedList(False)
Or1 = OrderedStringList(False)
Or1.add("a")
Or1.add(" a ")
Or1.add("a")
Or1.add("  ab ")
Or1.add("ab")
print(Or1.get_value())
print(Or1.find("a"))