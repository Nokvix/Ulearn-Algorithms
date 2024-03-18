from typing import Tuple

s = input()
length_s = len(s)


def find_substring(substring_length: int, quantity: int = 1) -> str | None:
    global s
    cur_substring = s[:substring_length]

    if substring_length == 1:
        for i in range(1, length_s):
            if cur_substring != s[i]:
                return None

    for i in range(1, quantity):
        left_border = i * substring_length
        right_border = left_border + substring_length

        if cur_substring != s[left_border:right_border]:
            return None

    return cur_substring


def find_result(substring_res: str, substring_counter: int) -> Tuple[int, str]:
    global length_s
    global s
    substring_res = s
    substring_counter = 1

    cur_substring = find_substring(1)
    if cur_substring:
        return length_s, cur_substring

    for i in range(2, length_s // 2 + 1):
        substring_length = length_s / i

        if substring_length % 1 == 0:
            substring_length = int(substring_length)
            cur_substring = find_substring(substring_length, i)

            if cur_substring:
                substring_res = cur_substring
                substring_counter = i
    return substring_counter, substring_res


substring_res = s
substring_counter = 1
substring_counter, substring_res = find_result(substring_res, substring_counter)

print(f"{substring_counter} {substring_res}")
