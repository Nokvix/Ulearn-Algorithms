# В некоторых местах сделана операция взятия остатка (%), тк могут передаваться номера вершин от 0 до n включительно.
# Чтобы не выходить за границы списка, пришлось использовать такой костыль :(

n = int(input())
neighbours_list = [None] * n
depth_list = [-1] * n
entrances = []
first_entrances = [-1] * n
last_entrances = [-1] * n


def fill_in_lists(tree_dict, vertex, parent, depth):
    if vertex is None:
        return
    global neighbours_list, depth_list, n

    vertex_module = vertex % n
    depth_list[vertex_module] = depth
    if vertex in tree_dict:
        neighbours_list[vertex_module] = tree_dict[vertex]
        if parent:
            neighbours_list[vertex_module].append(parent)
    else:
        neighbours_list[vertex_module] = [parent]
        return

    for child in tree_dict[vertex]:
        if child == parent:
            continue
        fill_in_lists(tree_dict, child, vertex, depth + 1)


def dfs(x, parent=None):
    global depth_list, neighbours_list, entrances, first_entrances, last_entrances

    x = x % n
    first_entrances[x] = len(entrances)
    entrances.append(x)
    for vertex in neighbours_list[x]:
        vertex_module = vertex % n
        if vertex_module != parent:
            dfs(vertex_module, x)
            entrances.append(x)
    last_entrances[x] = len(entrances)
    entrances.append(x)


def find_nearest_ancestor(a, b):
    global entrances, first_entrances, last_entrances, depth_list, n

    a = a % n
    b = b % n
    if first_entrances[a] > last_entrances[b]:
        b, a = a, b

    min_depth = n
    nearest_ancestor = n - 1
    for i in range(first_entrances[a], last_entrances[b]):
        vertex = entrances[i]
        if depth_list[vertex] < min_depth:
            min_depth = depth_list[vertex]
            nearest_ancestor = vertex
    return nearest_ancestor


def main():
    global n
    tree_dict = eval(input())
    a, b = map(int, input().split())
    keys = tree_dict.keys()
    root = None
    for key in keys:
        root = key
        break
    fill_in_lists(tree_dict, root, None, 0)
    dfs(root)
    result = find_nearest_ancestor(a, b)

    print(result)


main()
