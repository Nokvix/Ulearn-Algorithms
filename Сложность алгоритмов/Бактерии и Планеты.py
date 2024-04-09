def surviving_bacteria_on_planet(bacterial_temperatures, planetary_temperatures):
    surviving_dict = {}

    for i in range(len(planetary_temperatures)):
        surviving_dict[(planetary_temperatures[i], i)] = 0

    for min_temp, max_temp in bacterial_temperatures:
        for i in range(len(planetary_temperatures)):
            if min_temp <= planetary_temperatures[i] <= max_temp:
                surviving_dict[(planetary_temperatures[i], i)] += 1

    return surviving_dict


def main():
    n = int(input())
    bacterial_temperatures = []
    for _ in range(n):
        min_temp, max_temp = input().split()
        bacterial_temperatures.append((int(min_temp), int(max_temp)))
    planetary_temperatures = list(map(int, input().split()))

    surviving_dict = surviving_bacteria_on_planet(bacterial_temperatures, planetary_temperatures)

    for i in range(len(planetary_temperatures)):
        print(surviving_dict[(planetary_temperatures[i], i)])


main()
