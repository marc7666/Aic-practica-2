"""
Author names
"""
# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import math


def calc_impossible_pont(alt, distance_x, distance, height_aqueduct, pos_ant_x):
    """
    This method calculates the possibility of creating a bridge
    """

    radius = (distance / 2)
    height = math.sqrt((radius ** 2 - ((distance_x - pos_ant_x - radius) ** 2))) \
             + (height_aqueduct - radius)
    return height > alt


def calc_impossible(alt, distance, height_aqueduct):
    """
    This method calculates the possibility of creating an aqueduct
    """

    radius = (distance / 2)
    height = (height_aqueduct - radius)
    return height > alt


def obtain_values(values):
    """This method obtains de three different values:
    the distance between two columns (d), the different heights (coordinates Y),
    the different coordinates X
    """

    distance = []  # Distance
    distance_x = []  # Distance Coordinate Sol
    alt = []  # Height
    ant_dis = -50

    for pos in values:

        coordinate_x, coordinate_y = measures(pos)
        alt.append(coordinate_y)
        distance_x.append(coordinate_x)
        if ant_dis != -50:
            distance.append(coordinate_x - ant_dis)

        ant_dis = coordinate_x

    return distance, alt, distance_x


def obtain_distance(distance_x):
    """This method obtains de three different values:
    the distance between two columns (d), the different heights (coordinates Y),
    the different coordinates X
    """

    distance = []  # Distance
    ant_dis = -50

    if len(distance_x) == 2:
        distance.append(distance_x[len(distance_x) - 1] - distance_x[0])
    else:
        for pos in range(0, len(distance_x)):
            if ant_dis != -50:
                distance.append(distance_x[pos] - ant_dis)
            ant_dis = distance_x[pos]
    return distance


def measures(values):
    """
    This method returns a tuple with a the two coordinates of a terrain point
    """

    coordinate_x = values[0]
    coordinate_y = values[1]

    return coordinate_x, coordinate_y


def costs_aqueduct(terrain_points, alpha, beta, height_aqueduct, alt, distance):  # pylint: disable=R0913
    """
    This method calculates the costs of making an aqueduct
    """

    costs_alt = 0
    costs_dis = 0
    impossible = True

    for i in range(0, terrain_points):
        costs_alt += (height_aqueduct - alt[i])
        if i > 0:
            impossible = calc_impossible(alt[i], distance[i - 1], height_aqueduct)
        if i < terrain_points - 1:
            costs_dis += (distance[i] ** 2)
        if not impossible:
            break

    cost = (alpha * costs_alt) + (beta * costs_dis)
    # print(cost)
    return cost, impossible


def cost_pont(terrain_points, alpha, beta, height_aqueduct, alt, distance_x):  # pylint: disable=R0913
    """
    This method calculates the costs of making a bridge
    """

    costs_alt_pont = (height_aqueduct - alt[0]) + \
                     (height_aqueduct - alt[terrain_points - 1])
    d_pont = distance_x[terrain_points - 1] - distance_x[0]
    impossible = True

    for i in range(0, terrain_points):

        if i > 0:
            impossible = calc_impossible_pont(
                alt[i], distance_x[i], d_pont, height_aqueduct, distance_x[0]
            )

        if not impossible:
            break

    cost = ((alpha * costs_alt_pont) + (beta * (d_pont ** 2)))

    return cost, impossible
