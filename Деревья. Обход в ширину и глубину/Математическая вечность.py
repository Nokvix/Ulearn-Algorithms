from collections import deque


def increment(number, max_target_digit, length_number):
    digit_capacity = 10 ** (length_number - 1)
    digit = number // digit_capacity
    if digit < 9:
        if digit >= max_target_digit:
            return None
        new_number = number + digit_capacity
        return new_number
    return None


def decrement(number, min_target_digit):
    digit = number % 10
    if digit > 1:
        if digit <= min_target_digit:
            return None
        new_number = number - 1
        return new_number
    return None


def shift_to_right(number, length_number):
    last_digit = number % 10
    new_number = number // 10 + last_digit * 10 ** (length_number - 1)
    return int(new_number)


def shift_to_left(number, length_number):
    first_digit = number // 10 ** (length_number - 1)
    new_number = (number % 10 ** (length_number - 1)) * 10 + first_digit
    return int(new_number)


def convert_number(initial_number, target_number, max_target_digit, min_target_digit, length_number):
    visited = set()
    visited.add(initial_number)
    queue = deque([(initial_number, '')])

    while queue:
        current_number, commands = queue.popleft()

        for i in range(4):
            number = None
            match i:
                case 0:
                    number = increment(current_number, max_target_digit, length_number)
                case 1:
                    number = decrement(current_number, min_target_digit)
                case 2:
                    number = shift_to_right(current_number, length_number)
                case 3:
                    number = shift_to_left(current_number, length_number)

            if number:
                if number == target_number:
                    return commands + str(i)
                if number not in visited:
                    visited.add(number)
                    queue.append((number, commands + str(i)))


def main():
    initial_number = input().strip()
    target_number = input().strip()
    length_number = len(initial_number)

    max_target_digit = 0
    min_target_digit = 10
    for digit in target_number:
        digit = int(digit)
        if digit > max_target_digit:
            max_target_digit = digit
        if digit < min_target_digit:
            min_target_digit = digit

    initial_number, target_number = int(initial_number), int(target_number)
    commands = convert_number(initial_number, target_number, max_target_digit, min_target_digit, length_number)

    print(initial_number)
    current_number = initial_number
    for command in commands:
        match command:
            case '0':
                current_number = increment(current_number, max_target_digit, length_number)
            case '1':
                current_number = decrement(current_number, min_target_digit)
            case '2':
                current_number = shift_to_right(current_number, length_number)
            case '3':
                current_number = shift_to_left(current_number, length_number)
        print(current_number)


main()


# from collections import deque
#
#
# def increment(number, max_target_digit):
#
#     digit = int(number[0])
#     if digit < 9:
#         if digit >= max_target_digit:
#             return None
#         new_number = f"{digit + 1}{number[1:]}"
#         return new_number
#     return None
#
#
# def decrement(number, min_target_digit):
#
#     digit = int(number[-1])
#     if digit > 1:
#         if digit <= min_target_digit:
#             return None
#         new_number = f"{number[:-1]}{digit - 1}"
#         return new_number
#     return None
#
#
# def shift_to_right(number):
#     new_number = f"{number[-1]}{number[:-1]}"
#     return new_number
#
#
# def shift_to_left(number):
#     new_number = f"{number[1:]}{number[0]}"
#     return new_number
#
#
# def convert_number(initial_number, target_number, max_target_digit, min_target_digit):
#     visited = set()
#     visited.add(initial_number)
#     queue = deque([(initial_number, '')])
#
#     while queue:
#         current_number, commands = queue.popleft()
#
#         for i in range(4):
#             number = None
#             match i:
#                 case 0:
#                     number = increment(current_number, max_target_digit)
#                 case 1:
#                     number = decrement(current_number, min_target_digit)
#                 case 2:
#                     number = shift_to_right(current_number)
#                 case 3:
#                     number = shift_to_left(current_number)
#
#             if number:
#                 if number == target_number:
#                     return commands + str(i)
#                 if number not in visited:
#                     visited.add(number)
#                     queue.append((number, commands + str(i)))
#
#
# def main():
#     initial_number = input().strip()
#     target_number = input().strip()
#
#     max_target_digit = 0
#     min_target_digit = 10
#     for digit in target_number:
#         digit = int(digit)
#         if digit > max_target_digit:
#             max_target_digit = digit
#         if digit < min_target_digit:
#             min_target_digit = digit
#
#     commands = convert_number(initial_number, target_number, max_target_digit, min_target_digit)
#     print(initial_number)
#     current_number = initial_number
#     for command in commands:
#         match command:
#             case '0':
#                 current_number = increment(current_number, max_target_digit)
#             case '1':
#                 current_number = decrement(current_number, min_target_digit)
#             case '2':
#                 current_number = shift_to_right(current_number)
#             case '3':
#                 current_number = shift_to_left(current_number)
#         print(current_number)
#
#
# main()


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
