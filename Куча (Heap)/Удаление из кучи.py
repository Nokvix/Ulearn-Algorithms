import math


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

    def pop(self):
        index = self.size() - 1
        elem = self.min()

        self.heap[0], self.heap[index] = self.heap[index], self.heap[0]
        self.heap.pop(index)

        self.sift_down(0)

        return elem

    def sift_down(self, index):
        left = 2 * index + 1
        if left >= self.size():
            return
        right = 2 * index + 2

        min_son_index = left
        if right < self.size() and self.heap[left] > self.heap[right]:
            min_son_index = right

        if self.heap[min_son_index] >= self.heap[index]:
            return

        self.heap[index], self.heap[min_son_index] = self.heap[min_son_index], self.heap[index]
        self.sift_down(min_son_index)

    def structure(self):
        print('---STRUCTURE START---')
        layer = 0
        counter = 0
        current_numbers = []
        for elem in self.heap:
            counter += 1
            current_numbers.append(str(elem))

            if 2 ** layer == counter:
                print(' '.join(current_numbers))
                layer += 1
                counter = 0
                current_numbers = []

        if current_numbers:
            print(' '.join(current_numbers))

        print('---STRUCTURE END---')


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
            case 'pop':
                print(heap.pop())
            case 'structure':
                heap.structure()
            case 'exit':
                print('bye')
                break


main()
