def bubble_sort():
    numbers = list(map(int, input().split()))
    k = int(input())
    number_numbers = len(numbers)
    flag = True
    for i in range(number_numbers):
        if flag and i == k:
            flag = False
            print(' '.join(map(str, numbers)))

        for j in range(number_numbers - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(' '.join(map(str, numbers)))


bubble_sort()

