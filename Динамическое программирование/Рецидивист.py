def get_max(a, b):
    new_list = [a, b]
    new_list.sort(key=lambda x: (-(x[0] + x[1]), -x[0]))
    return new_list[0]


def find_max_cost(total_weight, cakes, n):
    costs_list = [(0, 0)] * n

    if cakes[0][1] <= total_weight:
        costs_list[0] = (cakes[0][1] * cakes[0][0], cakes[0][1])
    elif cakes[0][1] > total_weight and cakes[0][2] == 'Д':
        return cakes[0][0] * total_weight

    for i in range(1, n):
        for j in range(i):
            if cakes[i][1] > (total_weight - costs_list[j][1]) and cakes[i][2] == 'Н':
                costs_list[i] = get_max(costs_list[j], costs_list[i])

            elif cakes[i][1] > (total_weight - costs_list[j][1]) and cakes[i][2] == 'Д':
                current_cake = (costs_list[j][0] + (total_weight - costs_list[j][1]) * cakes[i][0], total_weight)
                costs_list[i] = get_max(costs_list[i], current_cake)

            else:
                current_cake = (costs_list[j][0] + cakes[i][3], costs_list[j][1] + cakes[i][1])
                costs_list[i] = get_max(costs_list[i], current_cake)

    return costs_list[-1][0]


def main():
    n, total_weight = map(int, input().split())
    cakes = []

    for _ in range(n):
        price, weight, cut = input().split()
        price, weight = int(price), int(weight)
        cakes.append((price / weight, weight, cut, price))

    cakes.sort(key=lambda x: -x[0])

    max_cost = str(round(find_max_cost(total_weight, cakes, n), 2))
    if max_cost == '0':
        max_cost += '.00'
    elif max_cost[-2] == '.':
        max_cost += '0'

    print(max_cost)


main()
