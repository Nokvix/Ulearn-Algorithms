import random


def partition(numbers, left, right):
    if right - left - 1 < 0:
        return left

    i = left
    j = right - 1
    random_value = random.randint(0, right - left)
    support_element = numbers[(left + random_value) % len(numbers)]
    while j - i >= 0:
        while numbers[i] < support_element:
            i += 1

        while numbers[j] > support_element:
            j -= 1

        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
        else:
            break

    return i


def find_kth_stat(numbers, k):
    left = 0
    right = len(numbers)
    while left + 1 < right:
        m = partition(numbers, left, right)
        if k >= m:
            left = m
        else:
            right = m

    return numbers[left]


def main():
    numbers = list(map(int, input().split()))
    k = int(input())
    kth = find_kth_stat(numbers, k)
    print(kth)


main()