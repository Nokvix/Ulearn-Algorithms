final_choice = []
maximum_calories = 0


def did_values_get_better(cur_choice, cur_calories):
    global final_choice, maximum_calories

    if cur_calories > maximum_calories:
        final_choice = cur_choice
        maximum_calories = cur_calories
    elif cur_calories == maximum_calories and len(cur_choice) > len(final_choice):
        final_choice = cur_choice
        maximum_calories = cur_calories


def select_dishes(n, budget, menu, cur_index, cur_choice, cur_calories, spent_money):
    if spent_money == budget:
        did_values_get_better(cur_choice, cur_calories)
        return
    elif spent_money < budget:
        did_values_get_better(cur_choice, cur_calories)

    for i in range(cur_index, n):
        if spent_money + menu[i][0] <= budget:
            select_dishes(n, budget, menu, i + 1, cur_choice + [menu[i][2]], cur_calories + menu[i][1],
                          spent_money + menu[i][0])

    return


def main():
    global final_choice, maximum_calories
    n, budget = map(int, input().split())
    menu = []
    for i in range(1, n + 1):
        price, calories = map(int, input().split())
        menu.append((price, calories, i))

    select_dishes(n, budget, menu, 0, [], 0, 0)
    print(len(final_choice), maximum_calories)
    print(*final_choice)


main()
