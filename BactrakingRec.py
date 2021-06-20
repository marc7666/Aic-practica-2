import calculs
import read_file
import arbol


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    impossible = True

    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])
    coste = arbol.Arbol.hijos(arbol.Arbol, 1, distance_x, alt, height_aqueduct, alpha, beta)

    return coste, impossible


if __name__ == "__main__":
    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test5-1.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)

    coste, impossible = backtracking(distance_x, alt, height_aqueduct, alpha, beta)
    print(arbol.Arbol.minimo)