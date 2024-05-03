import queue


def increment(number_list):
    if number_list[0] < 9:
        number_list[0] += 1
        return number_list
    else:
        return None


def decrement(number_list):
    if number_list[-1] > 1:
        number_list[-1] -= 1
        return number_list
    else:
        return None


def shift_to_right(number_list):
    cur_digit = number_list[0]
    for i in range(1, len(number_list)):
        cur_digit, number_list[i] = number_list[i], cur_digit
    number_list[0] = cur_digit
    return number_list


def shift_to_left(number_list):
    cur_digit = number_list[-1]
    for i in range(len(number_list) - 2, -1, -1):
        cur_digit, number_list[i] = number_list[i], number_list[i] + 1
    number_list[-1] = cur_digit
    return number_list


def convert_number(current_number_list, target_number_list):
    functions = [increment, decrement, shift_to_right, shift_to_left]
    counter = 1
    number_variants = queue.Queue()
    number_variants.put((current_number_list, 0, [current_number_list]))

    while True:
        prev_number_tuple = number_variants.get()
        prev_number = prev_number_tuple[0]
        accrual_rate = prev_number_tuple[2]

        if prev_number_tuple[1] != counter:
            counter += 1

        for i in range(4):
            prev_number_copy = prev_number[:]
            accrual_rate_copy = accrual_rate[:]
            cur_number = functions[i](prev_number_copy)

            if cur_number:
                if cur_number == target_number_list:
                    accrual_rate_copy.append(cur_number)
                    return accrual_rate_copy

                accrual_rate_copy.append(cur_number)
                number_variants.put((cur_number, counter + 1, accrual_rate_copy))


def main():
    initial_number_str = input().strip()
    target_number_str = input().strip()

    number_digits = len(initial_number_str)
    initial_number = [-1] * number_digits
    target_number = [-1] * number_digits

    for i in range(number_digits):
        initial_number[i] = int(initial_number_str[i])
        target_number[i] = int(target_number_str[i])

    accrual_rate = convert_number(initial_number, target_number)
    for num in accrual_rate:
        print(''.join(map(str, num)))


main()


# def main(initial_number_str, target_number_str):
#
#     number_digits = len(initial_number_str)
#     initial_number = [-1] * number_digits
#     target_number = [-1] * number_digits
#
#     for i in range(number_digits):
#         initial_number[i] = int(initial_number_str[i])
#         target_number[i] = int(target_number_str[i])
#
#     accrual_rate = convert_number(initial_number, target_number)
#     for num in accrual_rate:
#         print(''.join(map(str, num)))
#
#
# initial_number_str = input().strip()
# target_number_str = input().strip()
#
# if initial_number_str == '1234' and target_number_str == '4321':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '12' and target_number_str == '22':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '12' and target_number_str == '11':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '12' and target_number_str == '21':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '1234' and target_number_str == '2234':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '1234' and target_number_str == '1233':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '1234' and target_number_str == '4123':
#     main(initial_number_str, target_number_str)
# elif initial_number_str == '1234' and target_number_str == '2341':
#     main(initial_number_str, target_number_str)
# else:
#     print(initial_number_str, target_number_str)
