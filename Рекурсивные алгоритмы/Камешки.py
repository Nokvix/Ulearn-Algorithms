def merge(left_list, right_list):
    left_length = len(left_list)
    right_length = len(right_list)
    merged_list = []

    counter = 0
    i, j = 0, 0
    while i < left_length and j < right_length:
        if left_list[i] >= right_list[j]:
            counter += left_length - i
            merged_list.append(right_list[j])
            j += 1
        else:
            merged_list.append(left_list[i])
            i += 1

    merged_list.extend(left_list[i:])
    merged_list.extend(right_list[j:])

    return merged_list, counter


def list_division(list_numbers):
    list_numbers_length = len(list_numbers)

    if list_numbers_length < 2:
        return list_numbers, 0

    middle = list_numbers_length // 2
    left_list, left_counter = list_division(list_numbers[:middle])
    right_list, right_counter = list_division(list_numbers[middle:])

    merged_list, m_counter = merge(left_list, right_list)

    return merged_list, m_counter + left_counter + right_counter


def main():
    n = int(input())
    list_numbers = [int(input()) for _ in range(n)]
    total_list, counter = list_division(list_numbers)

    print(counter)


main()
