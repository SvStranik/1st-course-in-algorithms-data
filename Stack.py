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

def twoStach(s):
    stack1 = Stack()
    stack2 = Stack()
    for i in range(len(s)-1,-1,-1):
        stack1.push(s[i])
    while stack1.peek():
        if isinstance(stack1.peek(), int):
            per = stack1.peek()
        elif stack1.peek() == "+":
            per = 0
            while stack2.peek():
                per += stack2.pop()
        else:
            per = 1
            while stack2.peek():
                per *= stack2.pop()
        stack2.push(per)
        stack1.pop()
    return stack2.peek()

def equalityParentheses1(s):
    stack = Stack()
    if len(s) % 2 == 0 and s[0] == "(" :
        for i in range(len(s)):
            if s[i] == '(': stack.push(1)
    if stack.size() == len(s) / 2: return "сбалансированы"
    return "не сбалансированы"
