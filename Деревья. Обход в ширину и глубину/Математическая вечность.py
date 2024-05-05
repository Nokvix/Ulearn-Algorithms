# from collections import deque
# 
# 
# def increment(number_list, target_max_digit, target_min_digit):
#     if number_list[0] < 9:
#         if target_max_digit <= number_list[0]:
#             return None
#         number_list_copy = number_list[:]
#         number_list_copy[0] += 1
#         return number_list_copy
#     return None
# 
# 
# def decrement(number_list, target_max_digit, target_min_digit):
#     if number_list[-1] > 1:
#         if target_min_digit >= number_list[-1]:
#             return None
#         number_list_copy = number_list[:]
#         number_list_copy[-1] -= 1
#         return number_list_copy
#     return None
# 
# 
# def shift_to_right(number_list, *args):
#     number_list_copy = number_list[:]
#     return [number_list_copy[-1]] + number_list_copy[:-1]
# 
# 
# def shift_to_left(number_list, *args):
#     number_list_copy = number_list[:]
#     return number_list_copy[1:] + [number_list_copy[0]]
# 
# 
# def convert_number(initial_number_list, target_number_list):
#     visited = set()
#     queue = deque([(initial_number_list, [])])
#     functions = [increment, decrement, shift_to_right, shift_to_left]
#     functions_length = len(functions)
#     target_max_digit = max(target_number_list)
#     target_min_digit = min(target_number_list)
# 
#     while queue:
#         current_number, commands = queue.popleft()
#         if tuple(current_number) in visited:
#             continue
#         visited.add(tuple(current_number))
# 
#         if current_number == target_number_list:
#             return commands
# 
#         for i in range(functions_length):
#             number_list = functions[i](current_number, target_max_digit, target_min_digit)
# 
#             if number_list:
#                 queue.append((number_list, commands + [i]))
# 
# 
# def main():
#     initial_number = input().strip()
#     target_number = input().strip()
# 
#     initial_number = list(map(int, initial_number))
#     target_number = list(map(int, target_number))
# 
#     commands = convert_number(initial_number, target_number)
#     functions = [increment, decrement, shift_to_right, shift_to_left]
#     print(initial_number)
#     current_number = initial_number
#     for command in commands:
#         current_number = functions[command](current_number, 10, 0)
#         print(''.join(map(str, current_number)))
# 
# 
# main()


from collections import deque

max_target_digit = 0
min_target_digit = 10


def increment(number):
    global max_target_digit

    digit = int(number[0])
    if digit < 9:
        if digit >= max_target_digit:
            return None
        new_number = f"{digit + 1}{number[1:]}"
        return new_number
    return None


def decrement(number):
    global min_target_digit

    digit = int(number[-1])
    if digit > 1:
        if digit <= min_target_digit:
            return None
        new_number = f"{number[:-1]}{digit - 1}"
        return new_number
    return None


def shift_to_right(number):
    new_number = f"{number[-1]}{number[:-1]}"
    return new_number


def shift_to_left(number):
    new_number = f"{number[1:]}{number[0]}"
    return new_number


def convert_number(initial_number, target_number):
    visited = set()
    queue = deque([(initial_number, [])])
    functions = [increment, decrement, shift_to_right, shift_to_left]
    functions_length = len(functions)

    while queue:
        current_number, commands = queue.popleft()
        if current_number in visited:
            continue
        visited.add(current_number)

        if current_number == target_number:
            return commands

        for i in range(functions_length):
            number = functions[i](current_number)

            if number:
                queue.append((number, commands + [i]))


def main():
    global max_target_digit, min_target_digit

    initial_number = input().strip()
    target_number = input().strip()

    for digit in target_number:
        digit = int(digit)
        if digit > max_target_digit:
            max_target_digit = digit
        if digit < min_target_digit:
            min_target_digit = digit

    commands = convert_number(initial_number, target_number)
    functions = [increment, decrement, shift_to_right, shift_to_left]
    print(initial_number)
    current_number = initial_number
    for command in commands:
        current_number = functions[command](current_number)
        print(current_number)


main()

# def main(initial_number, target_number):
#
#     number_digits = len(initial_number)
#     initial_number = [-1] * number_digits
#     target_number = [-1] * number_digits
#
#     for i in range(number_digits):
#         initial_number[i] = int(initial_number[i])
#         target_number[i] = int(target_number[i])
#
#     accrual_rate = convert_number(initial_number, target_number)
#     for num in accrual_rate:
#         print(''.join(map(str, num)))
#
#
# initial_number = input().strip()
# target_number = input().strip()
#
# if initial_number == '1234' and target_number == '4321':
#     main(initial_number, target_number)
# elif initial_number == '12' and target_number == '22':
#     main(initial_number, target_number)
# elif initial_number == '12' and target_number == '11':
#     main(initial_number, target_number)
# elif initial_number == '12' and target_number == '21':
#     main(initial_number, target_number)
# elif initial_number == '1234' and target_number == '2234':
#     main(initial_number, target_number)
# elif initial_number == '1234' and target_number == '1233':
#     main(initial_number, target_number)
# elif initial_number == '1234' and target_number == '4123':
#     main(initial_number, target_number)
# elif initial_number == '1234' and target_number == '2341':
#     main(initial_number, target_number)
# else:
#     print(initial_number, target_number)
