import numpy as np
import DJkistra


def path_vec(src, end, index):
    print("path_mom")
    arena_mom_x = np.load("arena_mom_x.npy")
    arena_mom_y = np.load("arena_mom_y.npy")
    avg_x = np.sum(arena_mom_x, axis=0)
    avg_y = np.sum(arena_mom_y, axis=1)
    for i in range(5):
        c = 0
        d = 0
        for j in range(5):
            if arena_mom_x[j][i] != 0:
                c = c + 1
            if arena_mom_y[i][j] != 0:
                d = d + 1
        avg_x[i] = avg_x[i] / c
        avg_y[i] = avg_y[i] / d

    for i in range(5):
        for j in range(5):
            arena_mom_x[i][j] = avg_x[j]
            arena_mom_y[j][i] = avg_y[j]
    path = DJkistra.give_path(src, end, index)
    path_x = []
    path_y = []
    for i in range(len(path)):
        y = int(path[i] / 5)
        x = path[i] % 5
        path_x.append(arena_mom_x[y][x])
        path_y.append(arena_mom_y[y][x])
    print("path_x:", path_x, "\n", "path_y:", path_y)
    return path_x, path_y

path_vec