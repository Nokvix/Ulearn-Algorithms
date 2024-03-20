class PriorityQueue:
    def __init__(self):
        self.queue = dict()
        self.importance_list = []
        self.count = 0
        self.is_sorted = False

    def push(self, value, prior):
        if prior in self.queue:
            self.queue[prior].append(value)
        else:
            self.queue[prior] = [value]
        self.importance_list.append(prior)
        self.count += 1
        self.is_sorted = False

    def pop_top(self):
        if self.count > 0:
            if not self.is_sorted:
                self.importance_list.sort()
                self.is_sorted = True
            pop_prior = self.importance_list.pop()
            value = self.queue[pop_prior].pop(0)
            self.count -= 1
            return value
        return -1

    def size(self):
        return self.count

    def clear(self):
        self.queue = dict()
        self.importance_list = []
        self.count = 0

    def pop_all_k(self, prior):
        if prior not in self.queue:
            return -1
        res = self.queue[prior]
        self.queue[prior] = []
        self.count -= len(res)
        self.importance_list = list(filter(lambda x: x != prior, self.importance_list))

        return ' '.join(list(map(str, res))) if len(res) > 0 else -1

    def pop_k(self, prior):
        if prior in self.queue and len(self.queue[prior]) > 0:
            value = self.queue[prior].pop(0)
            self.importance_list.remove(prior)
            self.count -= 1
            return value
        else:
            return -1


def main():
    queue = PriorityQueue()
    commands = []

    while True:
        command = input()
        commands.append(command)
        command = command.split()
        match command[0]:
            case 'push':
                i, k = map(int, command[1:])
                queue.push(i, k)
                print('ok')
            case 'pop':
                if command[1] == 'top':
                    print(queue.pop_top())
                else:
                    print(queue.pop_k(int(command[1])))
            case 'popall':
                print(queue.pop_all_k(int(command[1])))
            case 'size':
                print(str(queue.size()))
            case 'clear':
                queue.clear()
                print('ok')
            case 'exit':
                print('bye')
                break


main()
