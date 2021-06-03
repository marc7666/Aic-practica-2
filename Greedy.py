import Stack
import calculs
import read_file


def greedy(n):
    arbol = []
    alt = [45, 63, 70, 61, 57]
    alture = []
    distance = []
    impossible = True
    alture.append(alt[0])
    arbol.append(n[0])
    minimo = 1e+100
    pos = 1
    i = 0
    # guardar_vec(arbol)
    print(arbol)

    while pos != len(n) - 1:

        i = i + 1
        if i < len(n):
            arbol.append(n[i])
            alture.append(alt[i])
            print(arbol)
            #print(alture)
            distance = calculs.obtain_distance(arbol)
            cost, impossible = calculs.costs_aqueduct(len(arbol), 78, 72, 169, alture, distance)
            print(cost)
            print(minimo)

            if cost < minimo:
                arbol.remove(n[i])
                alture.remove(alt[i])
                minimo = cost
                pos = i
            else:
                arbol.remove(n[i])
                alture.remove(alt[i])

        else:
            i = pos
            arbol.append(n[i])
            alture.append(alt[i])
            minimo = 1e+100
        #print(arbol)
        #print(pos)
    arbol.append(n[pos])
    alture.append(alt[pos])
    print(arbol)
    return minimo, impossible


if __name__ == "__main__":
    n = [7, 61, 67, 77, 87]
    cost, impossible = greedy(n)

    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test5-2.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)

    print(cost)


