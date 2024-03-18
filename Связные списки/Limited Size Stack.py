from collections import deque


class Stack:
    def __init__(self, limit: int):
        self.limit = limit
        self.stack = deque(maxlen=limit)

    def push(self, value):
        self.stack.appendleft(value)

    def pop(self):
        if self.stack:
            return self.stack.popleft()

    def count(self):
        return len(self.stack)


size_limiter = int(input())
stack = Stack(size_limiter)
output = []

while True:
    command_list = input().split()
    command = command_list[0]

    if command == 'push':
        stack.push(command_list[1])
        output.append('ok')
    elif command == 'pop':
        output.append(stack.pop())
    elif command == 'count':
        output.append(str(stack.count()))
    elif command == 'exit':
        output.append('bye')
        break

print('\n'.join(output))
