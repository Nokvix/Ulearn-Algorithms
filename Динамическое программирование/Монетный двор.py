def count_max_number_coins(n, m, tabel):
    for i in range(1, m):
        tabel[0][i] += tabel[0][i - 1]

    for i in range(1, n):
        tabel[i][0] += tabel[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            tabel[i][j] += max(tabel[i - 1][j], tabel[i][j - 1])

    return tabel[n - 1][m - 1]


def main():
    n, m = map(int, input().split())
    table = []

    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)

    max_number_coins = count_max_number_coins(n, m, table)
    print(max_number_coins)


main()
