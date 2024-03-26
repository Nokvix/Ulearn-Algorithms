def pebble_count(n, i, counter, list_numbers):
    if i == n - 1:
        return counter

    for j in range(i + 1, n):
        if list_numbers[i] >= list_numbers[j]:
            counter += 1
    return pebble_count(n, i + 1, counter, list_numbers)


def main():
    n = int(input())
    list_numbers = [int(input()) for _ in range(n)]
    counter = pebble_count(n, 0, 0, list_numbers)

    print(counter)


main()
