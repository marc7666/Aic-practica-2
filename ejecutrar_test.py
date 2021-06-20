"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+
import read_file
import arbol


def leer_ejecutar(i, j):
    """
    Reading de input file withe the data problem
    """

    num = "" + str(j)
    file = "testing/test" + str(i) + "-" + num + ".in"
    values, terrain_points, heihgt_aqueduct, alpha, beta = \
        read_file.read_file(file, data_separation=" ")

    return values, terrain_points, heihgt_aqueduct, alpha, beta


def escribir_ejecutar(i, j):
    """
    Reading de input file withe the data problem
    """
    num = "" + str(j)
    file = "testing/test" + str(i) + "-" + num + ".in"
    print("---------------------------------------")
    print("Fitx", file)
    print("---------------------------------------")
    print("Resultado introducido en el output.ans")
    print("---------------------------------------")
    print("Resultado RECURSIVO: ", arbol.Arbol.minimo)
    print("-------------------------")
    file_ans = open('output.ans', 'w')
    file_ans.write(str(arbol.Arbol.minimo) + '\n')
    file_ans.close()
    file = "testing/test" + str(i) + "-" + num + ".ans"

    with open(file) as file_a:
        content_a = set(file_a)
    with open("output.ans") as file_b:
        content_b = set(file_b)

    if content_b == content_a:
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
    num = "" + str(j)
    file = "testing/test" + str(i) + "-" + num + ".in"
    print("---------------------------------------")
    print("Fitx", file)
    print("---------------------------------------")
    print("Resultado introducido en el output.ans")
    print("---------------------------------------")
    print("Resultado RECURSIVO: ", coste)
    print("-------------------------")
    file_ans = open('output.ans', 'w')
    file_ans.write(str(coste) + '\n')
    file_ans.close()
    file = "testing/test" + str(i) + "-" + num + ".ans"

    with open(file) as file_a:
        content_a = set(file_a)
    with open("output.ans") as file_b:
        content_b = set(file_b)

    if content_b == content_a:
        print("OK")

    arbol.Arbol.arbol = []  # It will content the coordinates X of all the tree
    arbol.Arbol.alture = []  # It will save the coordinates Y of all the trees
    arbol.Arbol.impossible = True
    arbol.Arbol.minimo = 1e+100  # Minimum cost
    arbol.Arbol.dynamic = []  # It will content the X coordinates of the main branch
    arbol.Arbol.dynamic2 = []  # It will content the Y coordinates of the main branch
