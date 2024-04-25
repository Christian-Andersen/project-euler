import numpy as np
from copy import deepcopy


def is_path(graph: list[list], node_1: int, node_2: int, visted: set) -> bool:
    if node_1 == node_2:
        return True
    visted.add(node_1)
    for new_node in graph[node_1]:
        if new_node not in visted:
            if is_path(graph, new_node, node_2, visted):
                return True
    return False


def is_connected(graph: list[list]) -> bool:
    for node_1 in range(len(graph)):
        for node_2 in range(len(graph)):
            if not is_path(graph, node_1, node_2, set()):
                return False
    return True


def is_matrix_connected(matrix: np.ndarray) -> bool:
    visted = set([0])
    nodes = set([0])
    seen = set([0])
    while nodes:
        node = nodes.pop()
        visted.add(node)
        nodes.update(list(matrix[node].nonzero()[0]))
        seen.update(nodes)
        if len(seen) == 40:
            return True
        nodes.difference_update(visted)
    return len(matrix) == len(visted)


def are_edges_connected(edges: dict[tuple[int, int], int], size: int) -> bool:
    if not edges:
        return False
    edges_list = list(edges)
    visted = set(edges_list.pop())
    while edges_list:
        no_update = True
        new_edges_list = []
        for edge in edges_list:
            if (edge[0] in visted) or (edge[1] in visted):
                visted.update(edge)
                no_update = False
            else:
                new_edges_list.append(edge)
        if no_update:
            return False
        edges_list = new_edges_list
    if len(visted) == size:
        return True
    return False


matrix = []
with open('0107_network.txt', 'r') as file:
    for line in file:
        matrix.append([int(i)
                      for i in line.strip().replace('-', '0').split(',')])

all_edges = {}
for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j]:
            all_edges[(i, j)] = matrix[i][j]
old_total_wegith = sum(list(all_edges.values()))
all_edges = dict(sorted(all_edges.items(), key=lambda item: item[1]))

edge, weight = list(all_edges.items())[0]
new_edges = {edge: weight}
visted = set(edge)
while not are_edges_connected(new_edges, len(matrix)):
    for edge, weight in all_edges.items():
        test = (edge[0] in visted, edge[1] in visted)
        if all(test):
            continue
        if not any(test):
            continue
        new_edges[edge] = weight
        visted.update(edge)
        break


def edge_swap(edges, size):
    for removed_edge, removed_weight in edges.items():
        for new_edge, new_weight in all_edges.items():
            edges_copy = deepcopy(edges)
            if new_edge in edges_copy:
                continue
            if new_weight >= removed_weight:
                continue
            edges_copy.pop(removed_edge)
            edges_copy[new_edge] = new_weight
            if are_edges_connected(edges_copy, size):
                return edges_copy
    return None


print(old_total_wegith-sum(list(new_edges.values())))
while True:
    new_edges = edge_swap(new_edges, len(matrix))
    if new_edges is None:
        break
    print(old_total_wegith-sum(list(new_edges.values())))
