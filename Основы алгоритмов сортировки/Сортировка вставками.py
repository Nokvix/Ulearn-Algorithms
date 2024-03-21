def insertion_sorting():
    numbers = list(map(int, input().split()))
    len_numbers = len(numbers)

    for i in range(len_numbers):
        number = numbers.pop(i)
        for j in range(i):
            if numbers[j] > number:
                numbers.insert(j, number)
                break
        else:
            numbers.insert(i, number)
        if len_numbers % 2 == 0 and i == len_numbers // 2 - 1 or len_numbers % 2 == 1 and i == len_numbers // 2:
            print(' '.join(list(map(str, numbers))))
    print(' '.join(list(map(str, numbers))))


insertion_sorting()
