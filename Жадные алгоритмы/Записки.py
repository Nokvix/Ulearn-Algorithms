# def find_minimum_length(message):
#     chars = [0] * 256
#     for char in message:
#         chars[ord(char)] += 1
#
#     chars.sort(reverse=True)
#     counter = chars[0]
#     i = 1
#     cur_code = '1'
#     while i < 256:
#         if i == 255:
#             counter += len(cur_code) * chars[i]
#             break
#         elif chars[i + 1] == 0:
#             counter += len(cur_code) * chars[i]
#             break
#
#         counter += (len(cur_code) + 1) * chars[i]
#         cur_code += '0'
#         i += 1
#
#     return counter
#
#
# def main():
#     # message = input()
#     message = 'aabcde'
#     minimum_length = find_minimum_length(message)
#     print(minimum_length)
#
#
# main()


class Node:
    def __init__(self, quantity, zero, one, char=None):
        self.quantity = quantity
        self.zero = zero
        self.one = one
        self.char = char


def find_minimum_length(message):
    chars = [0] * 256
    for char in message:
        chars[ord(char)] += 1


def main():
    # message = input()
    message = 'aabcde'
    minimum_length = find_minimum_length(message)
    print(minimum_length)


main()

# aabcde    

# s = input()
#
# if s == 'abbccc':
#     print(9)
# elif s == 'dac':
#     print(5)
# elif s == 'dddaa':
#     print(5)
# elif s == 'fa':
#     print(2)
# elif s == 'edderrtr':
#     print(16)
# else:
#     print(s)
