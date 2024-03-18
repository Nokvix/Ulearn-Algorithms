from math import sqrt


def count_value(a, length, vo, vs):
    time = sqrt(length ** 2 + a ** 2) / vo + sqrt((1 - length) ** 2 + (1 - a) ** 2) / vs
    return time


def prepare_data_for_output(number, number_characters):
    number_zeros = 8 - number_characters
    return number + "0" * number_zeros


vo, vs = map(int, input().split())
a = int(input()) / 100
epsilon = 1e-7
x = epsilon / 2

right_edge = 1
left_edge = 0
position = 0
while right_edge - left_edge > epsilon:
    position = (left_edge + right_edge) / 2
    right_value = count_value(a, position + x, vo, vs)
    left_value = count_value(a, position - x, vo, vs)

    if right_value > left_value:
        right_edge = position
    else:
        left_edge = position

# position = str(round(position, 6))
# number_characters = len(position)
# if number_characters < 8:
#     position = prepare_data_for_output(position, number_characters)

print("{:.6f}".format(position))
