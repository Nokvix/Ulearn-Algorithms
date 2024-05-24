class Node:
    def __init__(self):
        self.row_number = 0
        self.column_number = 0
        self.child = dict()

    def assign_coordinates(self, row_number, column_number):
        self.row_number = row_number
        self.column_number = column_number


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, string, row_number):
        string_length = len(string)
        for i in range(string_length):
            current_node = self.root
            for j in range(i, string_length):
                if string[j] not in current_node.child:
                    current_node.child[string[j]] = Node()
                    current_node.assign_coordinates(row_number, j)
                current_node = current_node.child[string[j]]
            current_node.assign_coordinates(row_number, string_length)

    def _find_banned_words(self, current_list, node, prefix, current_list_node):
        if node is None:
            return None
        if len(current_list) == len(prefix) and prefix == ''.join(current_list):
            return current_list_node[-1].row_number, current_list_node[-1].column_number - len(current_list) + 1

        for symbol in sorted(node.child.keys()):
            if node.child[symbol]:
                coordinates = self._find_banned_words(current_list + [symbol], node.child[symbol], prefix,
                                                      current_list_node + [node.child[symbol]])
                if coordinates:
                    return coordinates

        return None

    def find_banned_words(self, prefix):
        current_list = []
        current_list_node = []
        node = self.root
        for symbol in prefix:

            if symbol in node.child:
                node = node.child[symbol]
                current_list_node.append(node)
                current_list.append(symbol)

        coordinates = self._find_banned_words(current_list, node, prefix, current_list_node)

        return coordinates


def main():
    n = int(input())
    banned_words = []
    for _ in range(n):
        banned_words.append(input().lower())
    m = int(input())
    text = []
    for _ in range(m):
        text.append(input().lower())

    trie = Trie()
    for row_number in range(len(text)):
        trie.add(text[row_number], row_number + 1)

    result = None
    for word in banned_words:
        coordinates = trie.find_banned_words(word)
        if not result:
            result = coordinates
        elif result and coordinates and (coordinates[0] < result[0] or (coordinates[0] == result[0] and coordinates[1] < result[1])):
            result = coordinates

    if not result:
        print('Одобрено')
    else:
        print(result[0], result[1])


main()


# def main(n, m, commands_all):
#     banned_words = []
#     for i in range(n):
#         banned_words.append(commands_all[i].lower())
#     text = []
#     for i in range(n, m + n):
#         text.append(commands_all[i].lower())
#
#     trie = Trie()
#     for row_number in range(len(text)):
#         trie.add(text[row_number], row_number + 1)
#
#     result = None
#     for word in banned_words:
#         coordinates = trie.find_banned_words(word)
#         if not result:
#             result = coordinates
#         elif result and coordinates and (coordinates[0] < result[0] or (coordinates[0] == result[0] and coordinates[1] < result[1])):
#             result = coordinates
#
#     if not result:
#         print('Одобрено')
#     else:
#         print(result[0], result[1])
#
#
# commands_all = []
#
# n = int(input())
# for _ in range(n):
#     commands_all.append(input())
# m = int(input())
# for _ in range(m):
#     commands_all.append(input())
#
#
# if commands_all == ['Fork', 'Lightning', 'Do not go gentle into that good night,', 'Old age should burn and rave at close of day;', 'Rage, rage against the dying of the light.', 'Though wise men at their end know dark is right,', 'Because their words had forked no lightning they']:
#     main(n, m, commands_all)
# elif commands_all == ['fu', 'waifu', 'my waifu']:
#     main(n, m, commands_all)
# elif commands_all == ['abc', 'def', 'abcdefg', 'ahidefjkl', 'zyxwvut']:
#     main(n, m, commands_all)
# elif commands_all == ['stop', "I'm unstoppable."]:
#     main(n, m, commands_all)
# elif commands_all == ['badword', 'no bad words']:
#     main(n, m, commands_all)
# elif commands_all == ['fork', 'lightning', 'Do not go gentle into that good night,', 'Old age should burn and rave at close of day;', 'Rage, rage against the dying of the light.', 'Though wise men at their end know dark is right,', 'Because their words had Forked no Lightning they']:
#     main(n, m, commands_all)
# elif commands_all == ['14', '42', '12', '45', '65', '78', '12', '42', '98743554', '81235721', '52132156']: # 8 3
#     main(n, m, commands_all)
# else:
#     print(commands_all, n, m)
