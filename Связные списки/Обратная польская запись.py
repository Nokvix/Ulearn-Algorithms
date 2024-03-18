from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.appendleft(value)

    def pop(self):
        if self.stack:
            return self.stack.popleft()


expression = input().split()
stack = Stack()

for obj in expression:
    if obj.isdigit():
        stack.push(int(obj))

    else:
        a = stack.pop()
        b = stack.pop()
        if obj == '+':
            stack.push(b + a)
        elif obj == '-':
            stack.push(b - a)
        elif obj == '*':
            stack.push(b * a)
        elif obj == '/':
            stack.push(b // a)
        elif obj == '%':
            stack.push(b % a)

print(stack.pop())
