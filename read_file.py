# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

def read_file(filename, data_separation=" "):
    print("---------- Reading file ----------")
    values = []  # List of tuples (x, y)
    # Opening file
    with open(filename, "r") as fn:
        # Strip lines
        strip_reader = (line.strip() for line in fn)
        filtered_reader = [line for line in strip_reader if line]
        # The firs line is the data of the problem
        n, h, alpha, beta = map(int, filtered_reader[0].split(data_separation))
        '''
        alpha and beta are the cost factors
        n is the number of tuples that form the ground
        h is the height of the aqueduct
        '''
        # Split lines, parse token and append to values
        for line in filtered_reader[1:]:
            '''
            x is the cartesian coordinate of a point of the ground
            y is the of the ordinate axis of a point of the ground  
            '''
            x, y = map(int, line.split(data_separation))
            values.append((x, y))
        return values, x, y, alpha, beta  # Returning the data of the problem
