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
import read_file
import arbol


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    """
       This method applies the backtracking strategy to resolve the problem.
       This is the recursive version
       """
    print("---------------------------------------")
    print(Fore.RED + "          Backtracking recursive" + Fore.RESET)
    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])
    arbol.Arbol.hijos(arbol.Arbol, 1, distance_x, alt, height_aqueduct, alpha, beta)


if __name__ == "__main__":

    i = 5
    j = 1
    for i in range(i, 8):
        for j in range(1, 4):

            VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = ejecutrar_test.leer_ejecutar(i, j)
            DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
            backtracking(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA)
            ejecutrar_test.escribir_ejecutar(i, j)
