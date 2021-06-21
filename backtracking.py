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


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    """
    This method applies the backtracking strategy to resolve the problem.
    This is the iterative version
    """
    print("---------------------------------------")
    print(Fore.BLUE + "             Backtracking " + Fore.RESET)
    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])

    for _ in range(1, len(distance_x)):
        arbol.Arbol.arbol.append(distance_x[_])
        arbol.Arbol.alture.append(alt[_])
        indice = distance_x.index(distance_x[_])
        arbol.Arbol.hijos(arbol.Arbol, indice + 1,
                          distance_x, alt, height_aqueduct, alpha, beta)
        arbol.Arbol.arbol.pop()
        arbol.Arbol.alture.pop()


if __name__ == "__main__":
    i = 5
    j = 1
    for i in range(i, 8):
        for j in range(1, 4):
            VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = \
                ejecutrar_test.leer_ejecutar(i, j)
            DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
            backtracking(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA)
            ejecutrar_test.escribir_ejecutar(i, j)
