"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import calculs
import read_file
import arbol


def backtracking(distance_x, alt, height_aqueduct, alpha, beta):
    """
    This method applies the backtracking strategy to resolve the problem.
    This is the iterative version
    """

    arbol.Arbol.arbol.append(distance_x[0])
    arbol.Arbol.alture.append(alt[0])
    if len(arbol.Arbol.arbol) == 2 and distance_x[len(distance_x) - 1] == \
            arbol.Arbol.arbol[len(arbol.Arbol.arbol) - 1]:
        pass
    for i in range(1, len(distance_x)):
        arbol.Arbol.arbol.append(distance_x[i])
        arbol.Arbol.alture.append(alt[i])
        indice = distance_x.index(distance_x[i])
        print(2)
        arbol.Arbol.hijos(arbol.Arbol, indice + 1,
                          distance_x, alt, height_aqueduct, alpha, beta)
        arbol.Arbol.arbol.pop()
        arbol.Arbol.alture.pop()


if __name__ == "__main__":
    VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = read_file.read_file("testing/test5-1.in",
                                                                               data_separation=" ")
    DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)

    backtracking(DISTANCE_X, ALT, HEIGHT_AQUEDUCT, ALPHA, BETA)
