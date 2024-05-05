class Heap:
    def __init__(self):
        self.heap = []

    def min(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def add(self, number):
        index = self.size()
        self.heap.append(number)
        self.sift_up(index)

    def sift_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.sift_up(parent)


def main():
    heap = Heap()
    while True:
        command = input().split()

        match command[0]:
            case 'add':
                heap.add(int(command[1]))
                print('ok')
            case 'min':
                print(heap.min())
            case 'size':
                print(heap.size())
            case 'exit':
                print('bye')
                break


main()
