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
        if not isinstance(value, list):
            if self.root is None:
                self.root = Node(value, None)
                return

            self._add(self.root, value)
        else:
            self.root = self.add_from_list(value)

    def add_from_list(self, numbers):
        list_numbers_length = len(numbers)
        if list_numbers_length == 0:
            return
        if list_numbers_length == 1:
            return Node(numbers[0], None)

        middle = list_numbers_length // 2
        if list_numbers_length % 2 == 0:
            middle -= 1
        node = Node(numbers[middle], None)
        node.left = self.add_from_list(numbers[:middle])
        node.right = self.add_from_list(numbers[middle + 1:])
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node

        return node

    def _find(self, node, value):
        if node is None:
            return
        if value == node.value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def find(self, value):
        return self._find(self.root, value)

    def _next(self, node):
        if not node:
            return
        if node.right:
            nxt = node.right
            while nxt.left:
                nxt = nxt.left
            return nxt

        nxt = node
        while nxt.parent and nxt.parent.right == nxt:
            nxt = nxt.parent
        return nxt.parent

    def next(self, value):
        cur_node = self.find(value)
        return self._next(cur_node)

    def _delete(self, node):
        if not node.left and not node.right:
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
            return

        if not node.left or not node.right:
            child = None
            if node.right:
                child = node.right
            elif node.left:
                child = node.left
            if node == self.root:
                self.root = child
                child.parent = None
            if node.parent.left == node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
            return

        if node.left and node.right:
            nxt = node.right
            while nxt.left:
                nxt = nxt.left
            node.value = nxt.value
            self._delete(nxt)
            return

    def delete(self, value):
        if not self.root:
            return

        node = self.find(value)
        if not node:
            return

        self._delete(node)

    def _get_min(self, node):
        if not node:
            return
        if not node.left:
            return node

        return self._get_min(node.left)

    def get_min(self):
        return self._get_min(self.root)

    def _get_max(self, node):
        if not node:
            return
        if not node.right:
            return node

        return self._get_max(node.right)

    def get_max(self):
        return self._get_max(self.root)

    def list(self):
        result = []
        cur_node = self.get_min()
        if not cur_node:
            return
        elem = self._next(cur_node)
        result.append(cur_node.value)
        while elem:
            result.append(elem.value)
            elem = self._next(elem)

        return result


def main():
    numbers = list(map(int, input().split()))
    tree = Tree()
    tree.add(numbers)

    while True:
        command = input().split()
        match command[0]:
            case 'add':
                tree.add(int(command[1]))
                print('Ok')
            case 'delete':
                tree.delete(int(command[1]))
                print('Ok')
            case 'find':
                res = tree.find(int(command[1]))
                if res:
                    print('Такая банка есть')
                else:
                    print('Такой банки нет')
            case 'min':
                res = tree.get_min()
                if res:
                    print(res.value)
                else:
                    print('Склад пуст')
            case 'max':
                res = tree.get_max()
                if res:
                    print(res.value)
                else:
                    print('Склад пуст')
            case 'list':
                res = tree.list()
                if res:
                    print(' '.join(list(map(str, res))))
                else:
                    print('')
            case 'exit':
                break


main()
