import calculs
import read_file
import Arbol


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    impossible = True
    coste = 0

    Arbol.Arbol.arbol.append(distance_x[0])
    Arbol.Arbol.alture.append(alt[0])
    if len(Arbol.Arbol.arbol) == 2 and distance_x[len(distance_x) - 1] == Arbol.Arbol.arbol[len(Arbol.Arbol.arbol) - 1]:
        return coste
    for i in range(1, 2):

        Arbol.Arbol.arbol.append(distance_x[i])
        Arbol.Arbol.alture.append(alt[i])
        indice = distance_x.index(distance_x[i])
        print(2)
        coste = Arbol.Arbol.hijos(Arbol.Arbol, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
        print(coste)
        Arbol.Arbol.arbol.pop()
        Arbol.Arbol.alture.pop()

    return coste, impossible


if __name__ == "__main__":
    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test5-1.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)

    coste, impossible = backtracking(distance_x, alt, height_aqueduct, alpha, beta)
    print()