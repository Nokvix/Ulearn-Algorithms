n = int(input())
neighbours_list = [None] * (n + 1)
depth_list = [-1] * (n + 1)
entrances = []
first_entrances = [-1] * (n + 1)
last_entrances = [-1] * (n + 1)


def fill_in_lists(tree_dict, vertex, parent, depth):
    if vertex is None:
        return
    global neighbours_list, depth_list, n

    depth_list[vertex] = depth
    if vertex in tree_dict:
        neighbours_list[vertex] = tree_dict[vertex]
        if parent:
            neighbours_list[vertex].append(parent)
    else:
        neighbours_list[vertex] = [parent]
        return

    for child in tree_dict[vertex]:
        if child == parent:
            continue
        fill_in_lists(tree_dict, child, vertex, depth + 1)


def dfs(x, parent=None):
    global depth_list, neighbours_list, entrances, first_entrances, last_entrances

    first_entrances[x] = len(entrances)
    entrances.append(x)
    for vertex in neighbours_list[x]:
        if vertex != parent:
            dfs(vertex, x)
            entrances.append(x)
    last_entrances[x] = len(entrances)
    entrances.append(x)


def find_nearest_ancestor(a, b):
    global entrances, first_entrances, last_entrances, depth_list, n

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
