class PowerSet:

    def __init__(self, sz = 100):
        self.Size = sz
        self.slots = [[] for _ in range(self.Size)]
        self.sizeSlot = 0


    def hash_fun(self, value):
         return sum(str(value).encode('utf-8')) % self.Size


    def seek_slot(self, value):
        if self.size() == self.Size:
            self.increaseSlots()
        self.slots[self.hash_fun(value)].append(value)
        self.sizeSlot += 1


    def increaseSlots(self):
        self.Size *= 2
        slots2 = [[] for _ in range(self.Size)]
        for i in range(len(self.slots)):
            for j in range(len(self.slots[i])):
                slots2[self.hash_fun(self.slots[i][j])].append(self.slots[i][j])
        self.slots = slots2
            

    def size(self):
        return self.sizeSlot


    def put(self, value):
        if not self.get(value):
            return self.seek_slot(value)


    def get(self, value):
        for i in self.slots[self.hash_fun(value)]:
            if i == value:
                return True
        return False


    def remove(self, value):
        list_slot = self.slots[self.hash_fun(value)]
        for i in range(len(list_slot)):
            if list_slot[i] == value:
                list_slot[i] = list_slot[len(list_slot)-1]
                list_slot.pop()
                self.sizeSlot -= 1
                return True
        return False
 

    def intersection(self, set2):
        resultat = []
        for i in set2:
            if self.get(i):
                resultat.append(i)
        if len(resultat) > 0: return resultat
        return None


    def union(self, set2):
        resultat = []
        for i in range(len(self.slots)):
            for j in range(len(self.slots[i])):
                resultat.append(self.slots[i][j])
        for j in set2:
            if not self.get(j):
                resultat.append(j)
        if len(resultat)>0: return resultat
        return None


    def difference(self, set2):
        resultat = []
        for i in range(len(self.slots)):
            for j in range(len(self.slots[i])):
                if self.slots[i][j] not in  set2:
                    resultat.append(self.slots[i][j])
        if len(resultat) > 0: return resultat
        return None



    def issubset(self, set2):
        for i in set2:
            if not self.get(i): return False
        return True


    def printSlots(self):
        resultat = []
        for i in range(len(self.slots)):
            for j in range(len(self.slots[i])):
                resultat.append(self.slots[i][j])
        return resultat
