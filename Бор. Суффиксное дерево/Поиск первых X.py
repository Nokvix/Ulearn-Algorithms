class Node:
    def __init__(self):
        self.is_end = False
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node()
        self.counter = 0
        self.is_empty = True

    def add(self, string):
        current_node = self.root
        for symbol in string:
            if symbol not in current_node.child:
                current_node.child[symbol] = Node()
            current_node = current_node.child[symbol]

        current_node.is_end = True
        self.is_empty = False

    def _get(self, count, current_list, node, prefix, result):
        if node is None:
            return None
        if node.is_end and len(current_list) > len(prefix):
            result.append(''.join(current_list))
            self.counter += 1
            if self.counter == count:
                return

        for symbol in sorted(node.child.keys()):
            if self.counter == count:
                return
            if node.child[symbol]:
                self._get(count, current_list + [symbol], node.child[symbol], prefix, result)

        if len(result) == 0:
            result.append('empty')

    def get(self, prefix, count):
        self.counter = 0
        current_list = []
        node = self.root
        result = []
        for symbol in prefix:
            if node is None or self.is_empty or symbol not in node.child:
                result.append('empty')
                return result

            node = node.child[symbol]
            current_list.append(symbol)

        self._get(count, current_list, node, prefix, result)

        return result


def main():
    trie = Trie()

    while True:
        command = input().split()

        match command[0]:
            case 'add':
                trie.add(command[1])
                print('ok')
            case 'get':
                result = trie.get(command[1], int(command[2]))
                print(' '.join(result))
            case 'exit':
                print('bye')
                break


main()
