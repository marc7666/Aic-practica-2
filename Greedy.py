import math


# n: number of points of the ground
# c: Dictionary that saves the coordinates tuples
# v0: Coordinate x of the last column

def greedy(n, c, v0=0):
    T = []
    B = [v0]
    v = v0
    while len(B) < n:
        minimum = 1e+100  # infinite cost
        for j in range(n):
            cost = c[(min(v, j), max(v, j))]
            if j not in B and cost < minimum:
                minimum = cost
                w = j
    B.append(w)
    T.append((v, w))
    v = w
    T.append((v, v0))
    return T
