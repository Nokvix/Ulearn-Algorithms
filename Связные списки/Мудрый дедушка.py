abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
weights_dict = dict()
freq_dict = dict()
outermost_part = []
middle_part = []


def process_data(weights, string):
    global weights_dict, freq_dict, outermost_part, middle_part, abc

    for i in range(len(weights)):
        weights_dict[abc[i]] = weights[i]

    dict_flag = dict()

    for letter in string:
        if letter in freq_dict:
            freq_dict[letter] += 1
            if freq_dict[letter] == 2 and weights_dict[letter] > 0:
                outermost_part.append(letter)
            elif freq_dict[letter] == 2 and weights_dict[letter] == 0:
                dict_flag[letter] = False
        else:
            freq_dict[letter] = 1
            dict_flag[letter] = True

    for letter in freq_dict.keys():
        if freq_dict[letter] == 1:
            middle_part.append(letter)
        if freq_dict[letter] > 2:
            number_of_letters = (freq_dict[letter] - 2) if dict_flag[letter] else freq_dict[letter]
            for _ in range(number_of_letters):
                middle_part.append(letter)


def prepare_response(weights, string):
    string_length = len(string)

    if all(weight == 0 for weight in weights):
        return f"{''.join(sorted(string))} 0"

    global freq_dict, weights_dict

    process_data(weights, string)

    if len(freq_dict.keys()) == 1 and weights_dict[list(freq_dict.keys())[0]] == 0:
        return f"{string} 0"

    sorted_outermost_part = sorted(outermost_part, key=lambda x: (-weights_dict[x], x))
    sorted_middle_part = sorted(middle_part)

    result_value = 0
    for i in range(len(sorted_outermost_part)):
        result_value += ((string_length - i - 1) - i) * weights_dict[sorted_outermost_part[i]]

    result_string_list = sorted_outermost_part + sorted_middle_part + sorted_outermost_part[::-1]

    return f"{''.join(result_string_list)} {result_value}"


def main():
    string = input()
    weights = list(map(int, input().split()))
    answer = prepare_response(weights, string)
    print(answer)


main()
