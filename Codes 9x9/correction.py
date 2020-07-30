import numpy as np

arena_mom_x = np.load("arena_mom_x.npy")
arena_mom_y = np.load("arena_mom_y.npy")
avg_x = np.sum(arena_mom_x, axis=0)
avg_y = np.sum(arena_mom_y, axis=1)
for i in range(9):
    c = 0
    d = 0
    for j in range(9):
        if arena_mom_x[j][i] != 0:
            c = c+1
        if arena_mom_y[i][j] != 0:
            d = d+1
    avg_x[i] = avg_x[i] / c
    avg_y[i] = avg_y[i] / d

for i in range(9):
    for j in range(9):
        arena_mom_x[i][j] = avg_x[j]
        arena_mom_y[j][i] = avg_y[j]

print(arena_mom_x, arena_mom_y)