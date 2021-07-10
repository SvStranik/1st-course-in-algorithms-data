class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size


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
        if None not in self.slots and key not in self.slots:
            index_slot = self.hits.index(min(self.hits))
            self.slots[index_slot] = key
            self.values[index_slot] = value
            self.hits[index_slot] = 0
        else:    
            while self.slots[index_slot] != None and self.slots[index_slot] != key:
                index_slot += 1
                if index_slot == self.size:index_slot = 0
            self.slots[index_slot] = key
            self.values[index_slot] = value
            self.hits[index_slot] += 1
     

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
