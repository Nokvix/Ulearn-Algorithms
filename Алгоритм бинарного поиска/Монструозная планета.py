def find_best_pos(millipede_list, multi_handle_list, l):
    favourable_pos = binary_position_search(millipede_list, multi_handle_list, l)

    if (favourable_pos != 0
            and (max(millipede_list[favourable_pos], multi_handle_list[favourable_pos]) >
                 max(millipede_list[favourable_pos - 1], multi_handle_list[favourable_pos - 1]))):
        favourable_pos -= 1

    favourable_pos = find_rightmost_pos(favourable_pos, l, millipede_list)

    return favourable_pos


def binary_position_search(millipede_list, multi_handle_list, l):
    left, right = 0, l - 1

    while left + 1 < right:
        middle = (right + left) // 2

        if millipede_list[middle] < multi_handle_list[middle]:
            left = middle
        else:
            right = middle

    return right


def find_rightmost_pos(favourable_pos, l, millipede_list):
    while (favourable_pos + 1 < l
           and millipede_list[favourable_pos] == millipede_list[favourable_pos + 1]):
        favourable_pos += 1
    return favourable_pos


def main():
    n, m, l = map(int, input().split())

    millipede_data = [list(map(int, input().split())) for _ in range(n)]
    multi_handle_data = [list(map(int, input().split())) for _ in range(m)]

    number_of_requests = int(input())
    for _ in range(number_of_requests):
        i, j = map(int, input().split())
        print(find_best_pos(millipede_data[i], multi_handle_data[j], l))


main()
