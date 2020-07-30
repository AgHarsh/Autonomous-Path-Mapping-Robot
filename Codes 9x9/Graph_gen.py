import numpy as np


def baap_baap(n, index):
    print("Running Graph_Gen.baap_baap")
    true_hoc = np.load("true_hoc.npy")
    weapons = np.load("weapons.npy")
    death_e = np.load("death_e.npy")
    jail = np.load("jail.npy")
    graph = np.zeros([n**2, n**2], dtype=int)
    not_all = []
    for i in range(n):
        for j in range(n):
            if true_hoc[i][j]:
                not_all.append(n*i + j)
    jails = []
    for i in range(n):
        for j in range(n):
            if jail[i][j] != 0:
                jails.append(n*i + j)
    for i in range(n):
        for j in range(n):
            if weapons[i][j]:
                not_all.append(n*i + j)
    for i in range(1, n**2 + 1):
        if i % n != 0:
            graph[i-1][i] = 100
            graph[i][i-1] = 100
            if i in not_all:
                graph[i-1][i] = 100000
                graph[i][i-1] = 100000
            if i in jails:
                graph[i-1][i] = 0
                graph[i][i-1] = 0
    for i in range(1, n*(n-1) + 1):
        graph[i-1][i+n-1] = 100
        graph[i+n-1][i-1] = 100
        if i in not_all:
            graph[i-1][i+n-1] = 100000
            graph[i+n-1][i-1] = 100000
        if i in jails:
            graph[i - 1][i+n-1] = 0
            graph[i+n-1][i - 1] = 0
    for i in index:
        for j in range(n**2):
            if graph[j][i] != 0:
                graph[j][i] = 1
    graph = graph.tolist()
    print("Graph:\n")
    print(graph)
    return graph
