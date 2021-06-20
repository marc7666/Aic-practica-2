"""
Importing calculs.py
"""
import calculs


class Arbol:  # pylint: disable=too-few-public-methods #pylint: disable=too-many-arguments
    """
    This class generates a tree and the method calculates the cost of every branch.
    """

    arbol = []  # It will content the coordinates X
    alture = []  # It will save the coordinates Y
    impossible = True  # It will mark if the tree is possible
    minimo = 1e+100  # Minimum cost
    dynamic = []  # It will content the all possibilities of every node

    def __init__(self, arbol, alture, impossible, minimo, dynamic):
        self.arbol = arbol
        self.alture = alture
        self.impossible = impossible
        self.minimo = minimo
        self.dynamic = dynamic

    def hijos(self, indice, distance_x, alt, height_aqueduct, alpha, beta):
        """
        This method just checks if a node has sons. If yes, it checks if the son have sons and
        if the first node doesn't have any sons the method goes to the previous node.
        """
        if indice < len(distance_x):  # Searching the all possible sons of every branch
            self.arbol.append(distance_x[indice])
            self.alture.append(alt[indice])
            self.arbol.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
            self.arbol.pop()
            self.alture.pop()
            self.arbol.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
        else:  # Calculating the cost of the branch
            if self.arbol[len(self.arbol) - 1] == distance_x[len(distance_x) - 1]:
                print("rama", indice, self.arbol)
                # print("rama alture", indice, self.alture)
                distance = calculs.obtain_distance(self.arbol)
                cost = calculs.costs_aqueduct(
                    len(self.arbol), alpha, beta, height_aqueduct, self.alture, distance)
                self.dynamic = self.dynamic + self.arbol
                print(self.dynamic)
                if cost < self.minimo:
                    self.minimo = cost
