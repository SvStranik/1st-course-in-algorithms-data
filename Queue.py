class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        queue = [item]
        for i in range(self.size()):
            queue.append(self.queue[i])
        self.queue = queue

    def dequeue(self):
        if self.size() != 0:
            queue = self.queue[self.size()-1]
            self.queue = self.queue[:self.size()-1]
            return queue
        return None 

    def size(self):
        size = len(self.queue)
        if size != 0: return size
        return 0
