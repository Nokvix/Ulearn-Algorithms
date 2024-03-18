first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))
frequency_dict = dict()

for number in first_array:
    if number not in frequency_dict:
        frequency_dict[number] = 0

for number in second_array:
    if number in frequency_dict:
        frequency_dict[number] += 1

result = []
for number in first_array:
    result.append(str(frequency_dict[number]))

print(' '.join(result))
