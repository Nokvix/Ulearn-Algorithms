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

    def _print_tree(self, node, cur_res, bool_list, depth, is_left):
        if not node:
            return

        if depth + 1 == len(bool_list):
            bool_list.append(True)

        string = ''.join(['│   ' if bool_res else '    ' for bool_res in bool_list[:depth]])
        string += '├───' if (is_left and node.parent.right) else '└───'
        string += str(node.value)
        cur_res.append(string)

        bool_list[depth + 1] = node.right is not None
        self._print_tree(node.left, cur_res, bool_list, depth + 1, True)
        bool_list[depth + 1] = False
        self._print_tree(node.right, cur_res, bool_list, depth + 1, False)

    def __str__(self):
        cur_res = [str(self.root.value)]
        bool_list = [True]
        self._print_tree(self.root.left, cur_res, bool_list, 0, True)
        bool_list[0] = False
        self._print_tree(self.root.right, cur_res, bool_list, 0, False)
        return '\n'.join(cur_res)

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


def main():
    numbers = list(map(int, input().split()))
    tree = Tree()
    tree.add(numbers)

    while True:
        command = input().split()
        match command[0]:
            case 'add':
                numbers = command[1:]
                for number in numbers:
                    tree.add(int(number))
                print('Ok')
            case 'delete':
                tree.delete(int(command[1]))
                print('Ok')
            case 'find':
                res = tree.find(int(command[1]))
                if res:
                    print('Число нашлось')
                else:
                    print('Число не нашлось')
            case 'next':
                res = tree.next(int(command[1]))
                if res:
                    print(res.value)
                else:
                    print('Следующего числа нет')
            case 'print':
                print(tree)
            case 'exit':
                break


main()
