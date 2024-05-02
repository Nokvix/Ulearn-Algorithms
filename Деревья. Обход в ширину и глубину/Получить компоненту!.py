class Node:
    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbours


def find_sequence(node, taken_vertices, result, nodes):
    taken_vertices[node.value] = True
    result.append(node.value)
    neighbours = node.neighbours

    for neighbour_value in neighbours:
        if not taken_vertices[neighbour_value]:
            find_sequence(nodes[neighbour_value], taken_vertices, result, nodes)


def main():
    n, v = map(int, input().split())
    nodes = []
    target_node = None
    taken_vertices = {}

    for i in range(n):
        neighbours = list(map(int, input().split()))

        if neighbours[0] == -1:
            neighbours = []
        node = Node(i, neighbours)

        if i == v:
            target_node = node
        nodes.append(node)
        taken_vertices[i] = False

    result = []
    find_sequence(target_node, taken_vertices, result, nodes)
    print(' '.join(list(map(str, sorted(result)))))


main()
