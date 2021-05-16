class Node: # Определяет узел
    def __init__(self,v):
        self.value = v # Само данное
        self.next = None # Связь

class LinkedList: # Создает связанный список
    def __init__(self):
        self.head = None
        self.tail = None
        
        def add_in_tail(self,item):
        # ДОБОВЛЯЕТ НОВЫЙ УЗЕЛ В КОНЦЕ СПИСКА    
            if self.head is None:
                self.head = item
            else:
                self.tail.next = item
            self.tail = item
            