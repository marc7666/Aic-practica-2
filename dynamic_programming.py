"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
from colorama import Fore
import calculs
import ejecutrar_test
import arbol


def dynamic_programming(distance_x, alt, height_aqueduct, alpha, beta):
    """
    This method applies the dynamic programming to solve the problem.
    This is the iterative version
    """
    print("---------------------------------------")
    print(Fore.BLUE + "         Dynamic Programming " + Fore.RESET)
    impossible = True
    res_distance = []
    res_alture = []
    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])
    arbol.Arbol.arbol.append(distance_x[1])
    arbol.Arbol.alture.append(alt[1])
    arbol.Arbol.hijos(arbol.Arbol, 2, distance_x, alt, height_aqueduct, alpha, beta)

    pos = 2
    for _ in range(2, len(arbol.Arbol.dynamic)):

        if arbol.Arbol.dynamic[pos] != distance_x[len(distance_x) - 1]:
            res_distance.append(arbol.Arbol.dynamic[pos])
            res_alture.append(arbol.Arbol.dynamic2[pos])
        else:
            res_distance.insert(0, distance_x[0])
            res_distance.append(distance_x[len(alt) - 1])
            res_alture.insert(0, alt[0])
            res_alture.append(alt[len(alt) - 1])

            distance = calculs.obtain_distance(res_distance)
            cost, impossible = calculs.costs_aqueduct(
                len(res_distance), alpha, beta, height_aqueduct, res_alture, distance)

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

    i = 5
    j = 1
    for i in range(i, 8):
        for j in range(1, 4):

            VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = ejecutrar_test.leer_ejecutar(i, j)
            DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
            IMPOSSIBLE = dynamic_programming(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA)
            ejecutrar_test.escribir_ejecutar(i, j)