# final_choice = []
# maximum_calories = 0
#
#
# def select_dishes(n, budget, menu):
#     table = [[0] * (budget + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for j in range(budget + 1):
#             if menu[i - 1][0] <= j:
#                 table[i][j] = max(menu[i - 1][1] + table[i - 1][budget - menu[i - 1][0]], table[i - 1][j])
#             else:
#                 table[i][j] = table[i - 1][j]
#
#     return table
#
#
# def main():
#     n, budget = map(int, input().split())
#     menu = []
#     for i in range(1, n + 1):
#         price, calories = map(int, input().split())
#         menu.append((price, calories, i))
#
#     # menu.sort(key=lambda x: x[0])
#     a = select_dishes(n, budget, menu)
#     print(a)
#
#
# main()


# def select_dishes(number_dishes, budget, menu):
#     # Создаем матрицу размером (number_dishes+1) x (budget+1) для хранения максимальной калорийности и списков заказанных блюд
#     table = [[(0, [])] * (budget + 1) for _ in range(number_dishes + 1)]
#
#     # Заполняем матрицу table
#     for i in range(1, number_dishes + 1):  # Перебираем все блюда
#         for j in range(1, budget + 1):  # Перебираем все возможные остатки бюджета
#             if menu[i - 1][0] <= j:  # Если цена текущего блюда не превышает остаток бюджета
#                 # Выбираем максимальное из двух вариантов:
#                 # 1. Калорийность текущего блюда + калорийность оставшегося бюджета, если блюдо выбрано
#                 # 2. Калорийность предыдущего блюда, если блюдо не выбрано
#                 if menu[i - 1][1] + table[i - 1][j - menu[i - 1][0]][0] > table[i - 1][j][0]:
#                     # Обновляем table, добавляя текущее блюдо в список заказанных блюд
#                     table[i][j] = (menu[i - 1][1] + table[i - 1][j - menu[i - 1][0]][0],
#                                 table[i - 1][j - menu[i - 1][0]][1] + [i])
#                 elif menu[i - 1][1] + table[i - 1][j - menu[i - 1][0]][0] == table[i - 1][j][0] and len(
#                         table[i - 1][j - menu[i - 1][0]][1]) >= len(table[i - 1][j][1]):
#                     table[i][j] = (menu[i - 1][1] + table[i - 1][j - menu[i - 1][0]][0],
#                                 table[i - 1][j - menu[i - 1][0]][1] + [i])
#                 else:
#                     table[i][j] = table[i - 1][j]  # Просто копируем значение из предыдущей строки
#             else:
#                 table[i][j] = table[i - 1][j]  # Просто копируем значение из предыдущей строки
#
#     # Находим максимальную калорийность и соответствующий список заказанных блюд
#     max_calories, num_dishes = table[number_dishes][budget]
#
#     # Возвращаем количество выбранных позиций, суммарную калорийность и список заказанных блюд
#     return len(num_dishes), max_calories, sorted(num_dishes)
#
#
# # Чтение входных данных
# number_dishes, budget = map(int, input().split())  # Читаем количество блюд и бюджет
# menu = []
# for _ in range(number_dishes):  # Читаем описание каждого блюда
#     price, calories = map(int, input().split())  # Цена и калорийность
#     menu.append((price, calories))
#
# # Вызов функции и вывод результата
# result = select_dishes(number_dishes, budget, menu)  # Вызываем функцию для решения задачи
# print(result[0], result[1])  # Выводим количество выбранных позиций и их суммарную калорийность
# print(*result[2])  # Выводим номера выбранных позиций через пробел


# def select_dishes(number_dishes, budget, menu):
#     # Создаем словарь для хранения результатов вычислений.
#     # Ключами словаря будут кортежи (i, j), где i - количество блюд,
#     # j - бюджет. Значениями будут кортежи (max_calories, num_dishes),
#     # где max_calories - максимальное количество калорий,
#     # num_dishes - список индексов блюд, которые позволят достичь max_calories.
#     table = {}
#
#     for i in range(number_dishes + 1):
#         for j in range(budget + 1):
#             if i == 0 or j == 0:
#                 # Инициализируем начальные значения как 0 калорий и пустой список блюд.
#                 table[(i, j)] = (0, [])
#             elif menu[i - 1][0] <= j:
#                 if menu[i - 1][1] + table[(i - 1, j - menu[i - 1][0])][0] > table[(i - 1, j)][0]:
#                     # Если добавление текущего блюда увеличивает общее количество калорий,
#                     # то обновляем значения в таблице.
#                     table[(i, j)] = (menu[i - 1][1] + table[(i - 1, j - menu[i - 1][0])][0],
#                                      table[(i - 1, j - menu[i - 1][0])][1] + [i])
#                 elif (menu[i - 1][1] + table[(i - 1, j - menu[i - 1][0])][0] == table[(i - 1, j)][0] and
#                       len(table[(i - 1, j - menu[i - 1][0])][1]) >= len(table[(i - 1, j)][1])):
#                     # Если добавление текущего блюда дает такое же количество калорий, но
#                     # меньше или равное количество блюд, то обновляем значения в таблице.
#                     table[(i, j)] = (menu[i - 1][1] + table[(i - 1, j - menu[i - 1][0])][0],
#                                      table[(i - 1, j - menu[i - 1][0])][1] + [i])
#                 else:
#                     # В противном случае просто копируем значения из предыдущей ячейки таблицы.
#                     table[(i, j)] = table[(i - 1, j)]
#             else:
#                 # Если стоимость текущего блюда превышает бюджет, то просто копируем значения
#                 # из предыдущей ячейки таблицы.
#                 table[(i, j)] = table[(i - 1, j)]
#
#     # Получаем результат из последней ячейки таблицы.
#     max_calories, num_dishes = table[(number_dishes, budget)]
#
#     return len(num_dishes), max_calories, sorted(num_dishes)
#
#
# # Считываем количество блюд и бюджет.
# number_dishes, budget = map(int, input().split())
# menu = []
# # Считываем стоимость и калорийность каждого блюда и сохраняем в список.
# for _ in range(number_dishes):
#     price, calories = map(int, input().split())
#     menu.append((price, calories))
#
# # Получаем результат и выводим.
# result = select_dishes(number_dishes, budget, menu)
# print(result[0], result[1])
# print(*result[2])


def select_dishes_recursive(number_dishes, budget, menu, i, j, table):
    # Базовый случай: если мы уже вычислили результат для этой ячейки,
    # просто возвращаем его.
    if (i, j) in table:
        return table[(i, j)]

    # Базовый случай: если не осталось блюд или бюджета, возвращаем 0 калорий и пустой список блюд.
    if i == 0 or j == 0:
        table[(i, j)] = (0, [])
        return table[(i, j)]

    # Если стоимость текущего блюда не превышает бюджет, мы можем рассмотреть два варианта:
    # либо берем текущее блюдо, либо не берем.
    if menu[i - 1][0] <= j:
        # Вариант, если берем текущее блюдо.
        with_curr_dish = select_dishes_recursive(number_dishes, budget, menu, i - 1, j - menu[i - 1][0], table)
        with_curr_dish = (with_curr_dish[0] + menu[i - 1][1], with_curr_dish[1] + [i])

        # Вариант, если не берем текущее блюдо.
        without_curr_dish = select_dishes_recursive(number_dishes, budget, menu, i - 1, j, table)

        # Выбираем вариант с максимальным количеством калорий.
        if with_curr_dish[0] > without_curr_dish[0] or (
                with_curr_dish[0] == without_curr_dish[0] and len(with_curr_dish[1]) >= len(without_curr_dish[1])):
            table[(i, j)] = with_curr_dish
        else:
            table[(i, j)] = without_curr_dish
    else:
        # Если стоимость текущего блюда превышает бюджет, просто идем к следующему блюду.
        table[(i, j)] = select_dishes_recursive(number_dishes, budget, menu, i - 1, j, table)

    return table[(i, j)]


def select_dishes(number_dishes, budget, menu):
    # Создаем словарь для хранения результатов вычислений.
    table = {}
    max_calories, num_dishes = select_dishes_recursive(number_dishes, budget, menu, number_dishes, budget, table)
    return len(num_dishes), max_calories, sorted(num_dishes)


# Считываем количество блюд и бюджет.
number_dishes, budget = map(int, input().split())
menu = []
# Считываем стоимость и калорийность каждого блюда и сохраняем в список.
for _ in range(number_dishes):
    price, calories = map(int, input().split())
    menu.append((price, calories))

# Получаем результат и выводим.
result = select_dishes(number_dishes, budget, menu)
print(result[0], result[1])
print(*result[2])
