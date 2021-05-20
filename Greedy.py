import math

# n: n ́umero de v ́ertices  del  grafo
# c: diccionario  de costes , indexado  por  aristas (i,j) con i<j

def greedy(n, c, v0=0):
    T = []
    B = [v0]
    v = v0
    while len(B) < n:
        minimo = 1e+100  # coste  infinito
        for j in range(n):
            # las  aristas  aparecen  en c como  tuplas (i,j) con i<j
            coste = c[(min(v, j), max(v, j))]
            if j not in B and coste < minimo:
                minimo = coste
                w = j
    B.append(w)
    T.append((v, w))
    v = w
    T.append((v, v0))
    return T
