import Stack
import calculs
import read_file


def greedy(distance_x, alt, height_aqueduct, alpha, beta):
    arbol = []
    alture = []
    impossible = True
    alture.append(alt[0])
    arbol.append(distance_x[0])
    minimo = 1e+100
    pos = 1
    i = 0
    # guardar_vec(arbol)
    print(arbol)

    while pos != len(distance_x) - 1:

        i = i + 1
        if i < len(distance_x):
            arbol.append(distance_x[i])
            alture.append(alt[i])
            print(arbol)
            #print(alture)
            distance = calculs.obtain_distance(arbol)
            cost, impossible = calculs.costs_aqueduct(len(arbol), alpha, beta, height_aqueduct, alture, distance)
            print(cost)
            print(minimo)

            if cost < minimo:
                arbol.remove(distance_x[i])
                alture.remove(alt[i])
                minimo = cost
                pos = i
            else:
                arbol.remove(distance_x[i])
                alture.remove(alt[i])

        else:
            i = pos
            arbol.append(distance_x[i])
            alture.append(alt[i])
            minimo = 1e+100
        #print(arbol)
        #print(pos)
    arbol.append(distance_x[pos])
    alture.append(alt[pos])
    print(arbol)
    return minimo, impossible


if __name__ == "__main__":

    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test5-5.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)
    cost, impossible = greedy(distance_x, alt, height_aqueduct, alpha, beta)
    print(cost)


