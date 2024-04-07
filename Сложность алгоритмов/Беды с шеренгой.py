# def partition(numbers, median, left, right):
#     if right - left - 1 < 0:
#         return left
#
#     i = left
#     j = right - 1
#     while j - i > 0:
#         while numbers[i] < median:
#             i += 1
#
#         while numbers[j] >= median:
#             j += 1
#
#         if i < j:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#         else:
#             break
#
#     return i
#
#
# def quick_sort(numbers, median, left, right):
#     median_pos = partition(numbers, median, left, right)
#     quick_sort(numbers, numbers[median_pos - 1], left, median_pos)
#     quick_sort(numbers, numbers[])
#
#
#
# def main():
#     numbers = list(map(int, input().split()))
#     quick_sort(numbers, numbers[-1], 0, len(numbers))
#     print(' '.join(list(map(str, numbers))))
#
#
# main()
#
#


def partition(numbers, median, left, right):
    if right - left - 1 < 0:
        return left

    i = left
    j = right - 1
    while j - i > 0:
        while numbers[i] < median:
            i += 1

        while numbers[j] > median:
            j -= 1

        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            break

    return i


def quick_sort(numbers, left, right):
    if right - left <= 1:
        return

    median = numbers[right - 1]
    print(median)
    median_pos = partition(numbers, median, left, right)
    quick_sort(numbers, left, median_pos)
    quick_sort(numbers, median_pos + 1, right)


def main():
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers))
    print(' '.join(map(str, numbers)))


main()
