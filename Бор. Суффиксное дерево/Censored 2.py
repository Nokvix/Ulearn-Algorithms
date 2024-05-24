class Node:
    def __init__(self):
        self.child = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, string):
        current_node = self.root

        for symbol in string:
            if symbol not in current_node.child:
                current_node.child[symbol] = Node()
            current_node = current_node.child[symbol]

        current_node.is_end = True

    def check_for_blocked_word(self, string, index):
        current_node = self.root
        string_length = len(string)
        for i in range(index, string_length + 1):
            if current_node.is_end:
                return index
            if i >= string_length:
                return None
            if not string[i].isalnum() or string[i] not in current_node.child:
                return None
            current_node = current_node.child[string[i]]
        return None


def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        trie.add(input().lower())

    m = int(input())
    column_index = None
    for i in range(m):
        string = input().lower()
        for index in range(len(string)):
            column_index = trie.check_for_blocked_word(string, index)
            if column_index is not None:
                print(i + 1, column_index + 1)
                break
        if column_index is not None:
            break

    if column_index is None:
        print('Одобрено')


main()
