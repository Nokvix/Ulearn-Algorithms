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
    return new_number


def shift_to_left(number, length_number):
    first_digit = number // 10 ** (length_number - 1)
    new_number = (number % 10 ** (length_number - 1)) * 10 + first_digit
    return new_number


def convert_number(initial_number, target_number, max_target_digit, min_target_digit, length_number):
    queue = deque([initial_number])
    path = [None] * 1000000
    path[initial_number] = -1
    while queue:
        current_number = queue.popleft()
        numbers = [increment(current_number, max_target_digit, length_number),
                   decrement(current_number, min_target_digit),
                   shift_to_right(current_number, length_number),
                   shift_to_left(current_number, length_number)]
        for number in numbers:
            if number == target_number:
                path[number] = current_number
                return path

            if number and not path[number]:
                path[number] = current_number
                queue.append(number)


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
    path = convert_number(initial_number, target_number, max_target_digit, min_target_digit, length_number)

    number = target_number
    result = []
    while number != -1:
        result.append(number)
        number = path[number]

    print('\n'.join(map(str, result[::-1])))


main()
