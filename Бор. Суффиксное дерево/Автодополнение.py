class Node:
    def __init__(self):
        self.is_end = False
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node()
        self.is_empty = True
        self.frequency_dict = dict()

    def add(self, string):
        current_node = self.root
        for symbol in string:
            if symbol not in current_node.child:
                current_node.child[symbol] = Node()
            current_node = current_node.child[symbol]

        if string not in self.frequency_dict:
            self.frequency_dict[string] = 0
        self.frequency_dict[string] += 1

        current_node.is_end = True
        self.is_empty = False

    def _get(self, current_list, node, prefix, result):
        if node is None:
            return None
        if node.is_end:
            current_string = ''.join(current_list)
            if result and self.frequency_dict[current_string] > self.frequency_dict[result]:
                result = current_string

            elif result and self.frequency_dict[current_string] == self.frequency_dict[result]:
                if len(current_list) < len(result) or (len(current_list) == len(result) and current_string < result):
                    result = current_string

            elif result is None:
                result = current_string

        for symbol in sorted(node.child.keys()):
            if node.child[symbol]:
                result = self._get(current_list + [symbol], node.child[symbol], prefix, result)

        return result

    def get(self, prefix):
        current_list = []
        node = self.root
        result = None
        for symbol in prefix:
            if node is None or self.is_empty or symbol not in node.child:
                return result

            node = node.child[symbol]
            current_list.append(symbol)

        result = self._get(current_list, node, prefix, result)

        return result


def main():
    trie = Trie()
    strings = input().split()
    for string in strings:
        trie.add(string)

    while True:
        command = input().split()

        match command[0]:
            case '+':
                trie.add(command[1])
                print('ok')
            case '?':
                result = ''
                if len(command) == 1:
                    result = trie.get('')
                else:
                    result = trie.get(command[1])
                print(result)
            case 'exit':
                print('bye')
                break


main()
