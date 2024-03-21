def selection_sorting():
    numbers = list(map(int, input().split()))
    len_numbers = len(numbers)

    for i in range(len_numbers):
        if i == len_numbers // 2:
            print(' '.join(list(map(str, numbers))))
        min_index = i
        for j in range(i + 1, len_numbers):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print(' '.join(list(map(str, numbers))))


selection_sorting()
