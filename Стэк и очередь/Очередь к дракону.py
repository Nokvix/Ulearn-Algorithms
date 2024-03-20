class Knight:
    def __init__(self, number):
        self.number = number
        self.back = None
        self.front = None


class Queue:
    def __init__(self):
        self.middle = None
        self.end = None
        self.start = None
        self.count = 0

    def push_end(self, number):
        new_knight = Knight(number)
        if self.start is None:
            self.start = new_knight
            self.middle = new_knight
        else:
            self.end.back = new_knight
            new_knight.front = self.end
            if self.count % 2 == 1:
                self.middle = self.middle.back

        self.end = new_knight
        self.count += 1

    def push_middle(self, number):
        new_knight = Knight(number)
        if self.start is None:
            self.start = new_knight
            self.middle = new_knight
            self.end = new_knight
        elif self.count % 2 == 1:
            prev = self.middle.back

            if prev:
                prev.front = new_knight
                new_knight.back = prev

            new_knight.front = self.middle
            self.middle.back = new_knight
            self.middle = new_knight

            if self.count == 1:
                self.end = new_knight
        elif self.count % 2 == 0:
            next_k = self.middle.front
            prev_k = self.middle

            if next_k:
                new_knight.front = next_k
                next_k.back = new_knight

            if prev_k:
                prev_k.front = new_knight
                new_knight.back = prev_k
            self.middle = new_knight

        self.count += 1

    def push_start(self, number):
        new_knight = Knight(number)
        if self.start is None:
            self.start = new_knight
            self.middle = new_knight
            self.end = new_knight
        else:
            new_knight.back = self.start
            self.start.front = new_knight
            self.start = new_knight
            if self.count % 2 == 0:
                self.middle = self.middle.front

        self.count += 1

    def pop(self):
        knight_number = self.start.number
        if self.count == 1:
            self.start = None
            self.end = None
            self.middle = None
            self.count -= 1
            return knight_number

        self.start = self.start.back
        if self.start:
            self.start.front = None

        if self.count % 2 == 1:
            self.middle = self.middle.back

        self.count -= 1
        return knight_number


def main():
    number_requests = int(input())
    output = []
    queue = Queue()

    for _ in range(number_requests):
        request = input().split()
        match request[0]:
            case '+':
                queue.push_end(int(request[1]))
            case '*':
                queue.push_middle(int(request[1]))
            case '!':
                queue.push_start(int(request[1]))
            case '-':
                output.append(str(queue.pop()))

    print('\n'.join(output))


main()
