total_length = 0


class PriorityQueue:
    def __init__(self):
        self.queue = dict()
        self.importance_list = []
        self.count = 0
        self.is_sorted = False

    def push(self, node):
        prior = node.quantity
        if prior in self.queue:
            self.queue[prior].append(node)
        else:
            self.queue[prior] = [node]
        self.importance_list.append(prior)
        self.count += 1
        self.is_sorted = False

    def pop(self):
        if self.count > 0:
            if not self.is_sorted:
                self.importance_list.sort(reverse=True)
                self.is_sorted = True
            pop_prior = self.importance_list.pop()
            node = self.queue[pop_prior].pop(0)
            self.count -= 1
            return node
        return -1

    def peek(self):
        if self.count > 0:
            if not self.is_sorted:
                self.importance_list.sort(reverse=True)
                self.is_sorted = True
            prior = self.importance_list[0]
            node = self.queue[prior][0]
            return node
        return -1

    def size(self):
        return self.count

    def clear(self):
        self.queue = dict()
        self.importance_list = []
        self.count = 0


class Node:
    def __init__(self, quantity, zero, one, char=None):
        self.quantity = quantity
        self.zero = zero
        self.one = one
        self.char = char


def build_tree(message):
    chars = [0] * 256
    for char in message:
        chars[ord(char)] += 1

    priority_queue = PriorityQueue()
    for i in range(len(chars)):
        if chars[i] > 0:
            node = Node(chars[i], None, None, chr(i))
            priority_queue.push(node)

    while priority_queue.size() > 1:
        node1 = priority_queue.pop()
        node2 = priority_queue.pop()
        new_node = Node(node1.quantity + node2.quantity, node1, node2)
        priority_queue.push(new_node)

    return priority_queue.peek()


def find_minimum_length(node, res):
    global total_length
    if node.zero is None:
        total_length += len(res) * node.quantity
        return

    find_minimum_length(node.zero, res + [0])
    find_minimum_length(node.one, res + [1])


def main():
    global total_length
    message = input()
    root_node = build_tree(message)
    if root_node.zero is not None:
        find_minimum_length(root_node, [])
    else:
        total_length += root_node.quantity

    print(total_length)


main()
