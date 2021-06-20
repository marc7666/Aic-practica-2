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
class Arbol:  # pylint: disable=R0903
    """
    This class generates a tree and the method calculates the cost of every branch.
    """

    arbol = []  # It will content the coordinates X
    alture = []  # It will save the coordinates Y
    impossible = True  # It will mark if the tree is possible
    minimo = 1e+100  # Minimum cost
    dynamic = []  # It will content the all possibilities of every node
    dynamic2 = []  # It will content the all possibilities of every node

    def __init__(self, arbol, alture, impossible, minimo, dynamic, dynamic2):
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
        if indice < len(distance_x):
            self.arbol.append(distance_x[indice])
            self.alture.append(alt[indice])
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
            self.arbol.pop()
            self.alture.pop()
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
            #print("hijo",indice, self.arbol)
        else:
            if self.arbol[len(self.arbol)-1] == distance_x[len(distance_x)-1]:
                print("rama", indice, self.arbol)
                distance = calculs.obtain_distance(self.arbol)
                cost, impossible = calculs.costs_aqueduct(len(self.arbol), alpha, beta, height_aqueduct, self.alture, distance)
                self.dynamic = self.dynamic + self.arbol
                self.dynamic2 = self.dynamic2 + self.alture

                #print(self.dynamic)
                if cost < self.minimo:
                    self.minimo = cost
                return self.minimo