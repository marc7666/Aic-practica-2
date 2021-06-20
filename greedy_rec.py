"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+
import calculs
import read_file
import arbol


def greedy(distance_x, alt, height_aqueduct, alpha, beta, i, pos):  # pylint: disable=too-many-arguments
    """
    This method aplies the greedy strategy to solve the problem
    """
    resultado = arbol.Arbol.minimo
    print(resultado)
    if arbol.Arbol.arbol[len(arbol.Arbol.arbol) - 1] != distance_x[len(distance_x) - 1]:
        if i < len(distance_x):
            arbol.Arbol.arbol.append(distance_x[i])
            arbol.Arbol.alture.append(alt[i])
            distance = calculs.obtain_distance(arbol.Arbol.arbol)
            print(arbol.Arbol.arbol)
            cost, impossible = calculs.costs_aqueduct(
                len(arbol.Arbol.arbol), alpha, beta, height_aqueduct, arbol.Arbol.alture, distance)

            if cost < arbol.Arbol.minimo:
                arbol.Arbol.arbol.remove(distance_x[i])
                arbol.Arbol.alture.remove(alt[i])
                arbol.Arbol.minimo = cost
                resultado = cost
                pos = i
            else:
                arbol.Arbol.arbol.remove(distance_x[i])
                arbol.Arbol.alture.remove(alt[i])
        else:
            i = pos
            arbol.Arbol.arbol.append(distance_x[i])
            arbol.Arbol.alture.append(alt[i])
            arbol.Arbol.minimo = 1e+100
        greedy(distance_x, alt, height_aqueduct, alpha, beta, i + 1, pos)

    else:
        return resultado, arbol.Arbol.impossible
    return resultado, arbol.Arbol.impossible


if __name__ == "__main__":
    VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = read_file.read_file(
        "testing/test5-1.in", data_separation=" ")
    DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
    arbol.Arbol.alture.append(ALT[0])
    arbol.Arbol.arbol.append(DISTANCE_X[0])
    COST, IMPOSSIBLE = greedy(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA, i=1, pos=1)
