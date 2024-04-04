def generate_sequences(k, m, n, current_sequence, combination):
    if k == 0:
        combination.append(' '.join(current_sequence))
        return

    for i in range(n, m - 1, -1):
        if i - m + 1 < k:
            continue
        generate_sequences(k - 1, m, i - 1, current_sequence + [str(i)], combination)


def main():
    combination = []
    k, m, n = map(int, input().split())
    generate_sequences(k, m, n, [], combination)

    print('\n'.join(combination[::-1]))
    print(len(combination))


main()
