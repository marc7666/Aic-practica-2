import calculs
import read_file
import Arbol


def DynamicProgramming(distance_x, alt, height_aqueduct, alpha, beta):
    impossible = True

    Arbol.Arbol.arbol.append(distance_x[0])
    Arbol.Arbol.alture.append(alt[0])
    Arbol.Arbol.arbol.append(distance_x[1])
    Arbol.Arbol.alture.append(alt[1])
    coste = Arbol.Arbol.hijos(Arbol.Arbol, 2, distance_x, alt, height_aqueduct, alpha, beta)

    return coste, impossible


if __name__ == "__main__":
    values, terrain_points, height_aqueduct, alpha, beta = read_file.read_file("testing/test5-1.in", data_separation=" ")
    distance, alt, distance_x = calculs.obtain_values(values)
    cost, impossible = DynamicProgramming(distance_x, alt, height_aqueduct, alpha, beta)

    print(cost)
