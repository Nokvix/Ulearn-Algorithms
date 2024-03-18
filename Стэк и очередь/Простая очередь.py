class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.counter = 0
        self.head = None

    def push(self, number):
        node = Node(number)

        if self.head is None:
            self.head = node
        else:
            self.head.next = node
        self.counter += 1
        return 'ok'

    def pop(self):
        if self.head.next is None:
            value = self.head.value
            self.head = None
        else:
            value = self.head.value
            self.head = self.head.next

        self.counter -= 1
        return value

    def front(self):
        return self.head.value

    def size(self):
        return self.counter

    def view(self):
        string = ''
        node = self.head
        if node is None:
            return string
        while True:
            if node.next is None:
                string += node.value
                return string
            else:
                string += f"{node.value}, "

    def clear(self):
        self.head = None
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
