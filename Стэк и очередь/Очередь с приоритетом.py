import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def push(self, value, prior):
        heapq.heappush(self.queue, (-prior, value))
        self.count += 1
        return 'ok'

    def pop_top(self):
        if self.count > 0:
            self.count -= 1
            return heapq.heappop(self.queue)[1]
        return '-1'

    def size(self):
        return self.count

    def clear(self):
        self.queue = []
        self.count = 0
        return 'ok'

    def exit(self):
        return 'bye'

    def pop_all_k(self, prior):
        res = []
        while self.count > 0 and self.queue and self.queue[0][0] <= -prior:
            elem = self.queue[0]
            if elem[0] == -prior:
                res.append(str(heapq.heappop(self.queue)[1]))
                self.count -= 1
            elif elem[0] > -prior:
                break

        if len(res) > 0:
            return ' '.join(res)
        return '-1'

    def pop_k(self, prior):
        for elem in self.queue:
            if elem[0] == -prior:
                return_val = elem[1]
                self.count -= 1
                self.queue.remove(elem)
                return return_val
            elif elem[0] > -prior:
                return '-1'
        else:
            return '-1'


def main():
    queue = PriorityQueue()
    output = []
    commands = []

    while True:
        command = input()
        commands.append(command)
        command = command.split()
        match command[0]:
            case 'push':
                i, k = map(int, command[1:])
                output.append(queue.push(i, k))
            case 'pop':
                if command[1] == 'top':
                    output.append(str(queue.pop_top()))
                else:
                    output.append(str(queue.pop_k(int(command[1]))))
            case 'popall':
                output.append(queue.pop_all_k(int(command[1])))
            case 'size':
                output.append(str(queue.size()))
            case 'clear':
                output.append(queue.clear())
            case 'exit':
                output.append(queue.exit())
                break

    print('\n'.join(output))


main()