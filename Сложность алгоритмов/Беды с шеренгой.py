def partition(numbers, left, right):
    if right - left <= 1:
        return left

    i = left
    j = right - 2
    support_element = numbers[right - 1]
    print(support_element)

    while i <= j:
        while numbers[i] < support_element:
            i += 1

        while numbers[j] >= support_element and j >= i:
            j -= 1

        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i], numbers[right - 1] = numbers[right - 1], numbers[i]
    return i


def quick_sort(numbers, left, right):
    if right - left <= 0:
        return

    m = partition(numbers, left, right)
    quick_sort(numbers, left, m)
    quick_sort(numbers, m + 1, right)


def main():
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers))
    print(' '.join(map(str, numbers)))


main()
