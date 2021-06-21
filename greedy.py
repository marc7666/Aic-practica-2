"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+
from colorama import Fore

import calculs
import ejecutrar_test


# pylint: disable=W0621
def greedy(distance_x, alt, height_aqueduct, alpha, beta):
    """
    This method aplies the greedy strategy to solve the problem
    """
    print("---------------------------------------")
    print(Fore.BLUE + "                 Greedy " + Fore.RESET)
    arbol = []
    alture = []
    impossible = True
    alture.append(alt[0])
    arbol.append(distance_x[0])
    minimo = 1e+100
    resultado = 1e+100
    pos = 1
    i = 0
    # guardar_vec(arbol)
    # print(arbol)

    while arbol[len(arbol) - 1] != distance_x[len(distance_x) - 1]:

        i = i + 1
        if i < len(distance_x):
            arbol.append(distance_x[i])
            alture.append(alt[i])
            #print(arbol)
            distance = calculs.obtain_distance(arbol)
            cost, impossible = calculs.costs_aqueduct(
                len(arbol), alpha, beta, height_aqueduct, alture, distance)
            # print(cost)
            # print(minimo)
            if cost < minimo:
                minimo = cost
                resultado = cost
                pos = i

            arbol.remove(distance_x[i])
            alture.remove(alt[i])
        else:
            i = pos
            arbol.append(distance_x[i])
            alture.append(alt[i])
            minimo = 1e+100

    # print(arbol)
    return resultado, impossible


if __name__ == "__main__":
    i = 5
    j = 1
    for i in range(i, 8):
        for j in range(1, 4):
            VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = \
                ejecutrar_test.leer_ejecutar(i, j)
            DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
            COST, IMPOSSIBLE = greedy(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA)
            ejecutrar_test.escribir_ejecutar2(i, j, COST)
