class Stack:
    def __init__(self):
        self.stack = []

    def top(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[len(self.stack) - 1]
        self.stack = self.stack[: len(self.stack) - 1]
        return item
