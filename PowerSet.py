class HashTable:
    def __init__(self, sz, stp):
        self.Size = sz
        self.step = stp
        if self.Size % self.step == 0: self.step += 1
        self.slots = [None] * self.Size
        self.arr_slot = []


    def hash_fun(self, value):
         return sum(value.encode('utf-8')) % self.Size


    def seek_slot2(self, value, per):
        arr = [None,value]
        index_slot = self.hash_fun(value)
        position = index_slot
        bool = False
        while position != index_slot or bool != True:
            if self.slots[position] == arr[per]: return position
            position += self.step
            if position >= self.Size:
                position -= self.Size
                bool = True
        return None


    def array_slot(self, value,add = True):
        if add == True: return self.arr_slot.append(value)
        index = self.arr_slot.index(value)
        arr_slot = []
        for i in range(len(self.arr_slot)):
            if i == index: continue
            arr_slot.append(self.arr_slot[i])
        self.arr_slot = arr_slot


class PowerSet(HashTable):


    def __init__(self,sz = 25000,stp = 201):
        super(PowerSet,self).__init__(sz,stp)


    def size(self):
        counter = 0
        for i in self.slots:
            if i != None:counter += 1
        return counter


    def put(self, value):
        if value not in self.arr_slot:
            position_slot = self.seek_slot2(value,0)
            self.slots[position_slot] = value
            self.array_slot(value)
        

    def get(self, value):
        index_slot = self.seek_slot2(value,1)
        if index_slot == None:return False
        else: return True
        

    def remove(self, value):
        index_slot = self.seek_slot2(value,1)
        if index_slot == None:
            return False
        else:
            self.slots[index_slot] = None
            self.array_slot(value,False)
            return True


    def intersection(self, set2):
        resultat = []
        for i in set2:
            if self.get(i) == True:
                resultat.append(i)
        if len(resultat)>0: return set(resultat)
        return None


    def union(self, set2):
        resultat = []
        for i in set2:
            if self.get(i) == False:
                resultat.append(i)
        set1 = self.printPw()
        for j in set1:
            resultat.append(j)
        if len(resultat)>0: return set(resultat)
        return None


    def difference(self, set2):
        resultat = []
        set1 = self.printPw()
        for j in set1:
            if j not in set2:
                resultat.append(j)
        if len(resultat)>0: return set(resultat)
        return None


    def issubset(self, set2):
        for i in set2:
            if self.get(i) == False: return False
        return True
