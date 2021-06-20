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
import arbol


# pylint: disable=R0913
# pylint: disable=E1121
# pylint: disable=R0903
class GreedyGlob:
    """
    This class generates a tree and the method calculates the cost of every branch.
    """

    i = 1
    pos = 1
    resultado = 0

    def __init__(self):
        self.i = 1
        self.pos = 1
        self.resultado = 0

    def greedy(self, distance_x, alt, height_aqueduct, alpha, beta):

        """
        This method aplies the greedy strategy to solve the problem
        """

        if arbol.Arbol.arbol[len(arbol.Arbol.arbol) - 1] != distance_x[len(distance_x) - 1]:
            if self.i < len(distance_x):
                arbol.Arbol.arbol.append(distance_x[self.i])
                arbol.Arbol.alture.append(alt[self.i])
                distance = calculs.obtain_distance(arbol.Arbol.arbol)
                # print(arbol.Arbol.arbol)
                cost, arbol.Arbol.impossible = \
                    calculs.costs_aqueduct(
                        len(arbol.Arbol.arbol), alpha, beta, height_aqueduct,
                        arbol.Arbol.alture, distance)

                if cost < arbol.Arbol.minimo:
                    arbol.Arbol.arbol.remove(distance_x[self.i])
                    arbol.Arbol.alture.remove(alt[self.i])
                    arbol.Arbol.minimo = cost
                    self.resultado = cost
                    self.pos = self.i
                else:
                    arbol.Arbol.arbol.remove(distance_x[self.i])
                    arbol.Arbol.alture.remove(alt[self.i])
            else:
                self.i = self.pos
                arbol.Arbol.arbol.append(distance_x[self.i])
                arbol.Arbol.alture.append(alt[self.i])
                arbol.Arbol.minimo = 1e+100

        else:
            return self.resultado, arbol.Arbol.impossible
        self.i = self.i + 1
        return self.greedy(self, distance_x, alt, height_aqueduct, alpha, beta)


if __name__ == "__main__":
    i = 5
    j = 1
    for i in range(i, 8):
        for j in range(1, 4):
            VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = \
                ejecutrar_test.leer_ejecutar(i, j)
            DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
            arbol.Arbol.alture.append(ALT[0])
            arbol.Arbol.arbol.append(DISTANCE_X[0])
            print("---------------------------------------")
            print(Fore.RED + "            Greedy recursive" + Fore.RESET)
            COST, IMPOSSIBLE = GreedyGlob.greedy(GreedyGlob, DISTANCE_X, ALT,
                                                 HEIGHT_AQUEDUCT, ALPHA, BETA)
            GreedyGlob.i = 1
            GreedyGlob.pos = 1
            GreedyGlob.resultado = 0
            ejecutrar_test.escribir_ejecutar2(i, j, COST)
