"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+
import sys
import read_file
import arbol


def leer_ejecutar(i, j):
    """
    Reading de input file withe the data problem
    """

    NUM = "" + str(j)
    FILE = "testing/test" + str(i) + "-" + NUM + ".in"
    VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA = read_file.read_file(FILE, data_separation=" ")

    return VALUES, TERRAIN_POINTS, HEIGHT_AQUEDUCT, ALPHA, BETA

def escribir_ejecutar(i, j):
    """
    Reading de input file withe the data problem
    """
    NUM = "" + str(j)
    FILE = "testing/test" + str(i) + "-" + NUM + ".in"
    print("---------------------------------------")
    print("Fitx", FILE)
    print("---------------------------------------")
    print("Resultado introducido en el output.ans")
    print("---------------------------------------")
    print("Resultado RECURSIVO: ", arbol.Arbol.minimo)
    print("-------------------------")
    file_ans = open('output.ans', 'w')
    file_ans.write(str(arbol.Arbol.minimo) + '\n')
    file_ans.close()
    FILE = "testing/test" + str(i) + "-" + NUM + ".ans"

    with open(FILE) as a:
        contentA = set(a)
    with open("output.ans") as b:
        contentB = set(b)

    if contentB == contentA:
        print("OK")

    arbol.Arbol.arbol = []  # It will content the coordinates X of all the tree
    arbol.Arbol.alture = []  # It will save the coordinates Y of all the trees
    arbol.Arbol.impossible = True
    arbol.Arbol.minimo = 1e+100  # Minimum cost
    arbol.Arbol.dynamic = []  # It will content the X coordinates of the main branch
    arbol.Arbol.dynamic2 = []  # It will content the Y coordinates of the main branch

def escribir_ejecutar2(i, j, coste):
    """
    Reading de input file withe the data problem
    """
    NUM = "" + str(j)
    FILE = "testing/test" + str(i) + "-" + NUM + ".in"
    print("---------------------------------------")
    print("Fitx", FILE)
    print("---------------------------------------")
    print("Resultado introducido en el output.ans")
    print("---------------------------------------")
    print("Resultado RECURSIVO: ", coste)
    print("-------------------------")
    file_ans = open('output.ans', 'w')
    file_ans.write(str(coste) + '\n')
    file_ans.close()
    FILE = "testing/test" + str(i) + "-" + NUM + ".ans"

    with open(FILE) as a:
        contentA = set(a)
    with open("output.ans") as b:
        contentB = set(b)

    if contentB == contentA:
        print("OK")

    arbol.Arbol.arbol = []  # It will content the coordinates X of all the tree
    arbol.Arbol.alture = []  # It will save the coordinates Y of all the trees
    arbol.Arbol.impossible = True
    arbol.Arbol.minimo = 1e+100  # Minimum cost
    arbol.Arbol.dynamic = []  # It will content the X coordinates of the main branch
    arbol.Arbol.dynamic2 = []  # It will content the Y coordinates of the main branch
