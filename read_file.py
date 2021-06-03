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
    # Openning file
    with open(filename, "r") as vec_file_name:
        # Strip lines
        strip_reader = (line.strip() for line in vec_file_name)
        filtered_reader = [line for line in strip_reader if line]
        # First line is the problem data
        terrain_points, height_aqueduct, alpha, beta = map(
            int, filtered_reader[0].split(data_separation)
        )
        # Split lines, parse token and append to values (2 to last)
        for line in filtered_reader[1:]:
            coordinate_x, coordinate_y = map(int, line.split(data_separation))
            values.append((coordinate_x, coordinate_y))
        return values, terrain_points, height_aqueduct, alpha, beta
