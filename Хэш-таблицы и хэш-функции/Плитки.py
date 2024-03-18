def is_equal(str1, str2):
    length = len(str1)
    for i in range(1, length + 1):
        if str1[i - 1] != str2[-i]:
            return False
    return True


# n, m = map(int, input().split())
# tiles = list(map(int, input().split()))
n, m = 6, 2
tiles = [1, 1, 2, 2, 1, 1]
possible_number_of_tiles = []

for position in range(n // 2 + 1):
    if position == 0:
        possible_number_of_tiles.append(str(n))
    elif tiles[position - 1] == tiles[position] and tiles[:position] == tiles[position:position * 2][::-1]:
        possible_number_of_tiles.append(str(n - position))
print(" ".join(possible_number_of_tiles))
