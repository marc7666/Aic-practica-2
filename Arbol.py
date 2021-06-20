import calculs

class Arbol:

    arbol = []
    alture = []
    impossible = True
    minimo = 1e+100
    dynamic = []

    def hijos(self, indice, distance_x, alt, height_aqueduct, alpha, beta):
        #print("subhijo", indice, self.arbol)
        if indice < len(distance_x):
            #print("subhijo", indice, self.arbol)
            self.arbol.append(distance_x[indice])
            self.alture.append(alt[indice])
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
            self.arbol.pop()
            self.alture.pop()
            # print("hijo", indice, self.arbol)
            self.hijos(self, indice + 1, distance_x, alt, height_aqueduct, alpha, beta)
            #print("hijo",indice, self.arbol)
        else:
            if self.arbol[len(self.arbol)-1] == distance_x[len(distance_x)-1]:
                print("rama", indice, self.arbol)
                #print("rama alture", indice, self.alture)
                distance = calculs.obtain_distance(self.arbol)
                cost, impossible = calculs.costs_aqueduct(len(self.arbol), alpha, beta, height_aqueduct, self.alture, distance)
                self.dynamic = self.dynamic + self.arbol
                print(self.dynamic)
                if cost < self.minimo:
                    self.minimo = cost
                return self.minimo



