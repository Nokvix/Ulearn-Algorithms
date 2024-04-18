class Gymnast:
    def __init__(self, name, power, weight):
        self.name = name
        self.power = int(power)
        self.weight = int(weight)
        self.amount = self.power + self.weight

    def __str__(self):
        return f"name: {self.name}, power: {self.power}, weight: {self.weight}, amount: {self.amount}"


def build_pyramid(gymnasts):
    pyramid = []
    total_weight = 0
    for gymnast in gymnasts:
        if gymnast.power >= total_weight:
            pyramid.append(gymnast)
            total_weight += gymnast.weight
        else:
            maximum_weight = 0
            maximum_weight_index = 0
            for i in range(len(pyramid)):
                if pyramid[i].weight > maximum_weight:
                    maximum_weight = pyramid[i].weight
                    maximum_weight_index = i

            if gymnast.weight <= maximum_weight:
                total_weight -= pyramid[maximum_weight_index].weight
                total_weight += gymnast.weight
                pyramid[maximum_weight_index] = gymnast
    return len(pyramid)


def main():
    n = int(input())
    gymnasts = []
    for _ in range(n):
        name, power, weight = input().split(';')
        gymnasts.append(Gymnast(name, power, weight))

    gymnasts.sort(key=lambda x: (x.amount, -x.weight))
    number_people = build_pyramid(gymnasts)

    print(number_people)


main()
