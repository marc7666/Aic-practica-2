"""
Author names
"""


# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************+


def read_file(filename, data_separation=" "):
    """
    Reading de input file withe the data problem
    """

    print("************* Fichero cargado *************")
    values = []  # List of tuples (x, y)
    # Opening file
    with open(filename, "r") as vec_file_name:  # Opening the file in read mode
        # Strip lines
        strip_reader = (line.strip() for line in vec_file_name)  # Putting all the file in a list
        # Putting all the lines of the file in a list
        filtered_reader = [line for line in strip_reader if line]
        # First line is the problem data
        terrain_points, height_aqueduct, alpha, beta = map(
            int, filtered_reader[0].split(data_separation)
        )
        # Split lines, parse token and append to values (2 to last)
        for line in filtered_reader[1:]:
            # Obtaining the coordinates of a point
            coordinate_x, coordinate_y = map(int, line.split(data_separation))
            # Aggregating the coordinates in the list
            values.append((coordinate_x, coordinate_y))
            # Returning the data file
        return values, terrain_points, height_aqueduct, alpha, beta
#