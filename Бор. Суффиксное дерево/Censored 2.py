class Node:
    def __init__(self, parent, previous_symbol):
        self.child = dict()
        self.is_end = False
        self.parent = parent
        self.previous_symbol = previous_symbol
        self.suffix_link = None
        self.transition = dict()


class Trie:
    def __init__(self):
        self.root = Node(None, None)

    def add(self, string):
        current_node = self.root
        for symbol in string:
            if symbol not in current_node.child:
                current_node.child[symbol] = Node(current_node, symbol)
            current_node = current_node.child[symbol]

        current_node.is_end = True

    def get_suffix_link(self, node):
        if node.suffix_link is None:
            if node == self.root or node.parent == self.root:
                node.suffix_link = self.root
            else:
                node.suffix_link = self.move_on(self.get_suffix_link(node.parent), node.previous_symbol)
        return node.suffix_link

    def move_on(self, node, symbol):
        if symbol not in node.transition:
            if symbol in node.child:
                node.transition[symbol] = node.child[symbol]
            elif node == self.root:
                node.transition[symbol] = self.root
            else:
                node.transition[symbol] = self.move_on(self.get_suffix_link(node), symbol)

        return node.transition[symbol]


def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        trie.add(input().lower())

    m = int(input())
    column_index = None
    for i in range(m):
        string = input().lower()
        node = trie.root
        for j in range(len(string)):
            node = trie.move_on(node, string[j])
            if node.is_end:
                column_index = j + 1
                print(i + 1, column_index)
                break
            if column_index is not None:
                break

    if column_index is None:
        print('Одобрено')


main()
