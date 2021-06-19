class NativeDictionary:
    def __init__(self, sz):
        self.size = sz # Размер
        self.slots = [None] * self.size # Ключ
        self.values = [None] * self.size #Значения соответствующие ключу

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size
        

    def is_key(self, key):
        index_slot = self.hash_fun(key)
        counter = 0
        while counter != self.size:
            if self.slots[index_slot] == key: return True
            index_slot += 1
            if index_slot == self.size:index_slot = 0
            counter += 1
        return False


    def put(self, key, value):
        index_slot = self.hash_fun(key)
        if None in self.slots or key in self.slots:
            while self.slots[index_slot] != None and self.slots[index_slot] != key:
                index_slot += 1
                if index_slot == self.size:index_slot = 0
            self.slots[index_slot] = key
            self.values[index_slot] = value
        else: None


    def get(self, key):
        index_slot = self.hash_fun(key)
        counter = 0
        while counter != self.size:
            if self.slots[index_slot] == key: 
                return self.values[index_slot]
            index_slot += 1
            if index_slot == self.size:index_slot = 0
            counter += 1
        return None
        