import calculs
import read_file
import arbol


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    impossible = True
    coste = 0

    arbol.arbol.arbol.append(distance_x[0])
    arbol.arbol.alture.append(alt[0])
    if len(arbol.arbol.arbol) == 2 and distance_x[len(distance_x) - 1] == arbol.arbol.arbol[len(arbol.arbol.arbol) - 1]:
        return coste
    for i in range(1, len(distance_x)):

        arbol.arbol.arbol.append(distance_x[i])
        arbol.arbol.alture.append(alt[i])
        indice = distance_x.index(distance_x[i])
        print(2)
        coste = arbol.arbol.hijos(arbol.arbol, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
        print(coste)
        arbol.arbol.arbol.pop()
        arbol.arbol.alture.pop()

    return coste, impossible


if __name__ == "__main__":
    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test18-10.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)

    coste, impossible = backtracking(distance_x, alt, height_aqueduct, alpha, beta)
    print()