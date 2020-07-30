import numpy as np


def jails(n, jail, death_e):
    jail_pos = []
    for i in range(n):
        for j in range(n):
            if jail[i][j] == 1:
                jail_pos.append(n * i + j)
    for i in range(n):
        for j in range(n):
            if jail[i][j] == 10:
                jail_pos.append(n * i + j)
    return jail_pos
