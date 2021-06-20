import random
import calculs
import calculsRecursive


def soil_generator(n):
    h = random.randint(150, 200)
    alpha = random.randint(1, 100)
    beta = random.randint(1, 100)

    points_x = sorted(random.sample(range(1, n * 10), n))
    print(n, h, alpha, beta)

    points = []
    for x in points_x:
        points.append((x, random.randint(1, 100)))

    return h, alpha, beta, points


def test_aqueducte(n):
    h, alpha, beta, points = soil_generator(n)
    xs, ys = list(zip(*points))
    calculs.calculate(n, h, alpha, beta, points)


def calcular_temps():
    import timeit
    temps = []
    for n in range(10, 300, 10):
        temps.append((n, timeit.timeit("test_aqueducte(" + str(n) + ")",
                                       setup="from __main__ import test_aqueducte", number=1000)))
    return temps


import matplotlib.pyplot as plt


def crear_grafica(x_list, y_list):
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
