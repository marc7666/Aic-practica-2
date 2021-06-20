"""
Importing calculs.py
"""
import calculs


# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+

# pylint: disable=too-many-arguments
# pylint: disable=E1121
class Arbol:  # pylint: disable=too-few-public-methods
    """
    This class generates a tree and the method calculates the cost of every branch.
    """

    arbol = []  # It will content the coordinates X of all the tree
    alture = []  # It will save the coordinates Y of all the trees
    impossible = True
    minimo = 1e+100  # Minimum cost
    dynamic = []  # It will content the X coordinates of the main branch
    dynamic2 = []  # It will content the Y coordinates of the main branch

    def __init__(self, arbol, alture, impossible, minimo, dynamic, dynamic2):
        # Initializing the variables
        self.arbol = arbol
        self.alture = alture
        self.impossible = impossible
        self.minimo = minimo
        self.dynamic = dynamic
        self.dynamic2 = dynamic2

    def hijos(self, indice, distance_x, alt, height_aqueduct, alpha, beta):
        """
        This method just checks if a node has sons. If yes, it checks if the son have sons and
        if the first node doesn't have any sons the method goes to the previous node.
        """
        if indice < len(distance_x):  # Generating all the possible sons, where indice = father node
            # distance_x = distances between X coordinates.
            self.arbol.append(distance_x[indice])
            self.alture.append(alt[indice])
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)  # Recursive call
            self.arbol.pop()
            self.alture.pop()
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)  # Recursive call
        else:  # Calculating the costs of every branch. Are the all the possible bridges
            if self.arbol[len(self.arbol) - 1] == distance_x[len(distance_x) - 1]:
                # print("rama", indice, self.arbol)
                distance = calculs.obtain_distance(self.arbol)
                cost, impossible = calculs.costs_aqueduct(
                    len(self.arbol), alpha, beta, height_aqueduct, self.alture, distance)
                self.impossible = impossible
                self.dynamic = self.dynamic + self.arbol
                self.dynamic2 = self.dynamic2 + self.alture

                if cost < self.minimo:
                    self.minimo = cost
