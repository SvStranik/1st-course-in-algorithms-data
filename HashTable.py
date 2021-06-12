class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size


    def hash_fun(self, value):
         return sum(value.encode('utf-8')) % self.size


    def seek_slot(self, value):
         index_slot = self.hash_fun(value)
         position = index_slot
         while position + self.step != index_slot:
              if self.slots[position] == None: return position
              if self.slots[position] == value: return position
              position += self.step
              if position > self.size - 1: position -= self.size
         return None


    def put(self, value):
         position_slot = self.seek_slot(value)
         if position_slot != None: 
              self.slots[position_slot] = value
              return position_slot
         return None 


    def find(self, value):
         index_slot = self.hash_fun(value)
         if self.slots[index_slot] == value : return index_slot
         position = index_slot + self.step
         if position > self.size - 1: position -= self.size
         while position != index_slot:
              if self.slots[position] == value: return position
              position += self.step
              if position > self.size - 1: position -= self.size
         return None
