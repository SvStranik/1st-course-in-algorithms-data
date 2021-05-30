class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            stack = self.stack[0]
            self.stack = self.stack[1:]
            return stack
        return None

    def push(self, value):
        new_stack = []
        new_stack.append(value)
        for i in range(self.size()):
            new_stack.append(self.stack[i])
        self.stack = new_stack[:]

    def peek(self):
        if self.size() != 0:
            return self.stack[0]
        return None 
