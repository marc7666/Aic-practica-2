import Stack
import calculs


def greedy(n):
    arbol = []
    impossible = True
    arbol.append(n[0])
    minimo = 1e+100
    pos = 1
    i = 0
    # guardar_vec(arbol)
    print(arbol)
    distance = [99, 45, 62, 20, 89]
    distan = []
    while pos != len(n) - 1:

        i = i + 1
        if i < len(n):
            arbol.append(n[i])
            distan.append(distance[i])
            print(arbol)
            cost, impossible = calculs.costs_aqueduct(len(arbol), 54, 67, 191, arbol, distan)
            print(cost)
            print(minimo)

            if cost < minimo:
                arbol.remove(n[i])
                distan.remove(distance[i])
                minimo = cost
                pos = i
            else:
                arbol.remove(n[i])
                distan.remove(distance[i])

        else:
            i = pos
            arbol.append(n[i])
            distan.append(distance[i])
            minimo = 1e+100
        print(arbol)
        print(pos)
    arbol.append(n[pos])
    distan.append(distance[pos])
    print(arbol)
    return minimo, impossible


def guardar_vec(arbol):
    lista2 = arbol.copy()
    alt = []

    for i in range(0, arbol.size()):
        alt.insert(0, lista2.top())
        lista2.pop()
    print(arbol.size())
    return alt


if __name__ == "__main__":
    n = [14, 16, 44, 75, 88]
    cost, impossible = greedy(n)
    print(cost)
