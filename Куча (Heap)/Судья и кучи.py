import math


class Heap:
    def __init__(self):
        self.heap = []

    def max(self):
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
        if self.heap[index][0] > self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.sift_up(parent)

    def pop(self):
        index = self.size() - 1
        elem = self.max()

        self.heap[0], self.heap[index] = self.heap[index], self.heap[0]
        self.heap.pop(index)

        self.sift_down(0)

        return elem

    def sift_down(self, index):
        left = 2 * index + 1
        if left >= self.size():
            return
        right = 2 * index + 2

        max_son_index = left
        if right < self.size() and self.heap[left][0] < self.heap[right][0]:
            max_son_index = right

        if self.heap[max_son_index][0] <= self.heap[index][0]:
            return

        self.heap[index], self.heap[max_son_index] = self.heap[max_son_index], self.heap[index]
        self.sift_down(max_son_index)


def main():
    heap = Heap()
    n, total_weight = map(int, input().split())
    total_price = 0

    for _ in range(n):
        price, weight = map(int, input().split())
        heap.add((price / weight, weight))

    while total_weight > 0 and heap.size() > 0:
        cake = heap.pop()
        if total_weight >= cake[1]:
            total_price += cake[0] * cake[1]
            total_weight -= cake[1]
        else:
            total_price += total_weight * cake[0]
            total_weight = 0

    str_total_cost = str(round(total_price, 2))
    if str_total_cost[-2] == '.':
        str_total_cost += '0'

    print(str_total_cost)


main()
