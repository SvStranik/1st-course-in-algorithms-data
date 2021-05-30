import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i != self.count:
            self.__getitem__(i)
        if self.count + 1 > self.capacity:
            new_capacity = (2 * self.capacity)
            self.resize(new_capacity)
        new_array = self.make_array(self.capacity)
        new_count = 0
        for j in range(self.count+1):
            if i == j:
                new_array[j] = itm
                continue
            new_array[j] = self.array[new_count]
            new_count += 1
        self.array = new_array
        

    def delete(self, i):
        self.__getitem__(i)
        new_array = self.make_array(self.capacity)
        per = 0
        for j in range(self.count):
            if j == i: 
                continue
            new_array[per] = self.array[j]
            per += 1
        self.array = new_array
        self.count -= 1
        if self.count < self.capacity // 2 and int(self.capacity / 1.5) >= 16:
            new_capacity = int(self.capacity / 1.5)
            self.resize(new_capacity)
