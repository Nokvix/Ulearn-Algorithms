from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, number):
        self.queue.append(number)
        return 'ok'

    def pop(self):
        return self.queue.popleft()

    def front(self):
        value = self.queue.popleft()
        self.queue.appendleft(value)
        return value

    def size(self):
        return len(self.queue)

    def view(self):
        return ', '.join(map(str, list(self.queue)))

    def clear(self):
        self.queue.clear()
        return 'ok'

    def exit(self):
        return 'bye'


def main():
    output = []
    queue = Queue()
    while True:
        command = input().split()

        match command[0]:
            case 'push':
                output.append(queue.push(int(command[1])))
            case 'pop':
                output.append(str(queue.pop()))
            case 'front':
                output.append(str(queue.front()))
            case 'size':
                output.append(str(queue.size()))
            case 'view':
                output.append(queue.view())
            case 'clear':
                output.append(queue.clear())
            case 'exit':
                output.append(queue.exit())
                break

    print('\n'.join(output))


main()
