"""
In this lab, you will build a function that converts an adjacency list representation of a graph into an adjacency matrix.
An adjacency list is a dictionary where each key represents a node, and the corresponding value is a list of nodes that the key node is connected to.
An adjacency matrix is a 2D array where the entry at position [i][j] is 1 if there's an edge from node i to node j, and 0 otherwise.
"""


def adjacency_list_to_matrix(adj_list):
    nb_lines = len(adj_list)
    print(nb_lines)
    result = []
    for i in range(nb_lines):
        line = []
        for j in range(nb_lines):
            if j in adj_list[i]:
                line.append(1)
            else:
                line.append(0)
        result.append(line)
    print(str(result))
    return result


adj_list = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}

adjacency_list_to_matrix(adj_list)
