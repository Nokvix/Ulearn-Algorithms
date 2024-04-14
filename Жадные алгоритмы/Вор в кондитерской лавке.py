class Cake:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume
        self.profitability = price / volume


def find_total_cost_cakes(cakes, package_volume):
    cakes.sort(key=lambda x: x.profitability, reverse=True)
    total_cost = 0.0
    for cake in cakes:
        if cake.volume <= package_volume:
            total_cost += cake.price
            package_volume -= cake.volume
        else:
            total_cost += cake.price * package_volume / cake.volume
            break

    return round(total_cost, 2)


def main():
    n, package_volume = map(int, input().split())
    cakes = []

    for _ in range(n):
        price, volume = map(int, input().split())
        cake = Cake(price, volume)
        cakes.append(cake)

    total_cost = find_total_cost_cakes(cakes, package_volume)
    str_total_cost = str(total_cost)
    if str_total_cost[-2] == '.':
        str_total_cost += '0'
    print(str_total_cost)


main()
