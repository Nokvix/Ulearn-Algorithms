class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def _add(self, node, value):
        if node is None:
            return

        if value < node.value:
            if node.left is None:
                node.left = Node(value, node)
                return
            self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value, node)
                return
            self._add(node.right, value)

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
            return

        self._add(self.root, value)

    def add_from_list(self, numbers, tree):
        list_numbers_length = len(numbers)
        if list_numbers_length == 0:
            return
        if list_numbers_length == 1:
            tree.add(numbers[0])
            return

        middle = list_numbers_length // 2
        if list_numbers_length % 2 == 0:
            middle -= 1
        value = numbers[middle]
        tree.add(value)

        self.add_from_list(numbers[:middle], tree)
        self.add_from_list(numbers[middle + 1:], tree)

    def _print_tree(self, node, prefix=[], is_left=True):
        if node:
            self._print_tree(node.right, prefix + ["│   " if is_left else "    "], False)
            print("".join(prefix) + ("└─── " if is_left else "├─── ") + str(node.value))
            self._print_tree(node.left, prefix + ["    " if is_left else "│   "], True)

    def print_tree(self):
        self._print_tree(self.root)


def main():
    numbers = list(map(int, input().split()))
    tree = Tree()
    tree.add_from_list(numbers, tree)
    tree.print_tree()


main()
