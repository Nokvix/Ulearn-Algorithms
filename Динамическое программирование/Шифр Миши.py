def encrypt_with_minimum_length(s):
    n = len(s)
    substring_table = [["" for _ in range(n)] for _ in range(n)]

    for substring_length in range(1, n + 1):
        for i in range(n - substring_length + 1):
            j = i + substring_length - 1
            substring = s[i:j + 1]
            substring_table[i][j] = substring

            for k in range(i, j):
                if len(substring_table[i][k] + substring_table[k + 1][j]) < len(substring_table[i][j]):
                    substring_table[i][j] = substring_table[i][k] + substring_table[k + 1][j]

            for k in range(1, substring_length):
                repeating_string = substring[:k]
                if substring_length % k == 0 and repeating_string * (substring_length // k) == substring:
                    encoded_str = f"{substring_length // k}({substring_table[i][i + k - 1]})"
                    if len(encoded_str) < len(substring_table[i][j]):
                        substring_table[i][j] = encoded_str

    return substring_table[0][n - 1]


def main():
    string = input()
    print(encrypt_with_minimum_length(string))


main()
