def surviving_bacteria_on_planet(bacterial_temperatures, planetary_temperatures):
    surviving_dict = {}
    for planet_temp in planetary_temperatures:
        if planet_temp not in surviving_dict:
            surviving_dict[planet_temp] = 0

    for min_temp, max_temp in bacterial_temperatures:
        for planet_temp in planetary_temperatures:
            if min_temp <= planet_temp <= max_temp:
                surviving_dict[planet_temp] += 1

    return surviving_dict


def main():
    n = int(input())
    bacterial_temperatures = []
    for _ in range(n):
        min_temp, max_temp = input().split()
        bacterial_temperatures.append((int(min_temp), int(max_temp)))
    planetary_temperatures = list(map(int, input().split()))

    surviving_dict = surviving_bacteria_on_planet(bacterial_temperatures, planetary_temperatures)

    for planet_temp in surviving_dict:
        print(surviving_dict[planet_temp])


main()
