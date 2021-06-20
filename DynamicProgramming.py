import calculs
import read_file
import arbol


def DynamicProgramming(distance_x, alt, height_aqueduct, alpha, beta):
    impossible = True
    res_distance = []
    res_alture = []
    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])
    arbol.Arbol.arbol.append(distance_x[1])
    arbol.Arbol.alture.append(alt[1])
    coste = arbol.Arbol.hijos(arbol.Arbol, 2, distance_x, alt, height_aqueduct, alpha, beta)

    print(arbol.Arbol.dynamic)
    pos = 2
    for i in range(2, len(arbol.Arbol.dynamic)):

        if (arbol.Arbol.dynamic[pos] != distance_x[len(distance_x) - 1]):
            res_distance.append(arbol.Arbol.dynamic[pos])
            res_alture.append(arbol.Arbol.dynamic2[pos])
        else:
            res_distance.insert(0, distance_x[0])
            res_distance.append(distance_x[len(alt) - 1])
            res_alture.insert(0, alt[0])
            res_alture.append(alt[len(alt) - 1])

            distance = calculs.obtain_distance(res_distance)
            cost, impossible = calculs.costs_aqueduct(len(res_distance), alpha, beta, height_aqueduct, res_alture, distance)


            if cost < arbol.Arbol.minimo:
                arbol.Arbol.minimo = cost

            if len(res_distance) == 2:
                break

            pos = pos + 2
            res_distance = []
            res_alture = []

        pos = pos + 1
    return impossible

if __name__ == "__main__":
    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file(
        "testing/test5-1.in", data_separation=" ")

    distance, alt, distance_x = calculs.obtain_values(values)
    impossible = DynamicProgramming(distance_x, alt, height_aqueduct, alpha, beta)
    print(impossible)
    print(arbol.Arbol.minimo)
