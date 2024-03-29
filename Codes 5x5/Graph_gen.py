import numpy as np


def generate_graph(index):
    true_hoc = np.load("true_hoc.npy")
    weapons = np.load("weapons.npy")
    graph = np.zeros([25, 25], dtype=int)
    not_all = []
    for i in range(5):
        for j in range(5):
            if true_hoc[i][j]:
                not_all.append(5*i + j)
    for i in range(5):
        for j in range(5):
            if weapons[i][j]:
                not_all.append(5*i + j)
    for i in range(1, 26):
        if i % 5 != 0:
            graph[i-1][i] = 50
            graph[i][i-1] = 50
            if i in not_all:
                graph[i-1][i] = 10000
                graph[i][i-1] = 10000
    for i in range(1, 21):
        graph[i-1][i+4] = 50
        graph[i+4][i-1] = 50
        if i in not_all:
            graph[i-1][i+4] = 10000
            graph[i+4][i-1] = 10000
    for i in index:
        for j in range(25):
            if graph[j][i] != 0:
                graph[j][i] = 1
    graph = graph.tolist()
    return graph
