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


# pylint: disable=R0913
# pylint: disable=E1121
# pylint: disable=R0903

class Dynamic:
    """
    This class generates a tree and the method calculates the cost of every branch.
    """

    res_distance = []
    res_alture = []
    pos = 2

    def __init__(self):
        self.res_distance = []
        self.res_alture = []
        self.pos = 1

    def dynamic_programming(self, distance_x, alt, height_aqueduct, alpha, beta):
        """
        This method applies the dynamic programming to solve the problem.
        This is the iterative version
        """

        if self.pos == 2:
            arbol.Arbol.arbol.append(distance_x[0])
            arbol.Arbol.alture.append(alt[0])
            arbol.Arbol.arbol.append(distance_x[1])
            arbol.Arbol.alture.append(alt[1])
            arbol.Arbol.hijos(arbol.Arbol, 2, distance_x, alt, height_aqueduct, alpha, beta)

        if self.pos < len(arbol.Arbol.dynamic):
            if arbol.Arbol.dynamic[self.pos] != distance_x[len(distance_x) - 1]:
                self.res_distance.append(arbol.Arbol.dynamic[self.pos])
                self.res_alture.append(arbol.Arbol.dynamic2[self.pos])
            else:

                self.res_distance.insert(0, distance_x[0])
                self.res_distance.append(distance_x[len(alt) - 1])
                self.res_alture.insert(0, alt[0])
                self.res_alture.append(alt[len(alt) - 1])
                distance = calculs.obtain_distance(self.res_distance)
                # print(self.res_distance)
                cost, arbol.Arbol.impossible = calculs.costs_aqueduct(
                    len(self.res_distance), alpha, beta, height_aqueduct, self.res_alture, distance)

                if cost < arbol.Arbol.minimo:
                    arbol.Arbol.minimo = cost

                self.pos = self.pos + 2
                self.res_distance = []
                self.res_alture = []

            self.pos = self.pos + 1
        else:
            return arbol.Arbol.minimo

        return self.dynamic_programming(self, distance_x, alt, height_aqueduct, alpha, beta)


if __name__ == "__main__":
    VALUES, TERRAIN_POINTS, HEIGHT_AQUEDCUT, ALPHA, BETA = read_file.read_file(
        "testing/test6-1.in", data_separation=" ")

    DISTANCE, ALT, DISTANCE_X = calculs.obtain_values(VALUES)
    COSTE = Dynamic.dynamic_programming(Dynamic, DISTANCE_X, ALT, HEIGHT_AQUEDCUT, ALPHA, BETA)
    print(COSTE)
