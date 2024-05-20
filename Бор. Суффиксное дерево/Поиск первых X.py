class Node:
    def __init__(self):
        self.is_end = False
        self.child = [None] * 256

    def get_or_create_node(self, index):
        if not self.child[index]:
            self.child[index] = Node()

        return self.child[index]


class Trie:
    def __init__(self):
        self.root = Node()
        self.counter = 0

    def add(self, string):
        current_node = self.root
        for symbol in string:
            current_node = current_node.get_or_create_node(ord(symbol))

        current_node.is_end = True

    def _get(self, count, current_list, node, prefix, result):
        if node is None:
            return None
        if node.is_end and len(current_list) > len(prefix):
            result.append(''.join(current_list))
            self.counter += 1
            if self.counter == count:
                return

        child = node.child
        for i in range(len(child)):
            if self.counter == count:
                return
            if child[i]:
                self._get(count, current_list + [chr(i)], child[i], prefix, result)

    def get(self, prefix, count):
        current_list = []
        node = self.root
        result = []
        for symbol in prefix:
            if node is None:
                result.append('empty')
                return result

            node = node.child[ord(symbol)]
            current_list.append(symbol)

        self._get(count, current_list, node, prefix, result)

        if self.counter == count:
            self.counter = 0

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
