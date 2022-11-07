# aoc.year2021.cuboid

class Cuboid:
    """ 
    Cuboid class.
    Stores the coordinates that limit the cuboid.
    """

    # The init method or constructor
    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z, start_state):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z
        self.state = start_state


    def count_state(self):
        """Calculates the size of the cuboid.
        """
        # I think we are always working with regular shapes
        size_x = abs(self.min_x - self.max_x) + 1
        size_y = abs(self.min_y - self.max_y) + 1
        size_z = abs(self.min_z - self.max_z) + 1
        volume = size_x * size_y * size_z
        return volume


    def print(self):
        """Prints the cuboid.
        """
        cuboid_to_str = f"x={self.min_x}..{self.max_x}, y={self.min_y}..{self.max_y}, z={self.min_z}..{self.max_z} state={self.state}"
        print(cuboid_to_str)


    def copy(self):
        c = Cuboid(self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z, self.state)
        return c


    def split(self, axis, value):
        c1 = self.copy()
        c2 = self.copy()
        if axis == 'x':
            c1.max_x = value
            c2.min_x = value + 1 # so they don't intersect
        if axis == 'y':
            c1.max_y = value
            c2.min_y = value + 1
        if axis == 'z':
            c1.max_z = value
            c2.min_z = value + 1
        return [c1, c2]

def cuboid_intersect_x(c1, c2):
    x_values = []
    if c2.min_x >= c1.min_x and c2.min_x <= c1.max_x:
        x_values.append(c2.min_x)
    if c2.max_x >= c1.min_x and c2.max_x <= c1.max_x:
        x_values.append(c2.max_x)
    return x_values

def cuboid_intersect_y(c1, c2):
    y_values = []
    if c2.min_y >= c1.min_y and c2.min_y <= c1.max_y:
        y_values.append(c2.min_y)
    if c2.max_y >= c1.min_y and c2.max_y <= c1.max_y:
        y_values.append(c2.max_y)
    return y_values

def cuboid_intersect_z(c1, c2):
    z_values = []
    if c2.min_z >= c1.min_z and c2.min_z <= c1.max_z:
        z_values.append(c2.min_z)
    if c2.max_z >= c1.min_z and c2.max_z <= c1.max_z:
        z_values.append(c2.max_z)
    return z_values

def cuboid_intersect(c1, c2):
    result = {}
    result_x = cuboid_intersect_x(c1, c2)
    result_y = cuboid_intersect_y(c1, c2)
    result_z = cuboid_intersect_z(c1, c2)
    if len(result_x) > 0:
        result['x'] = result_x
    if len(result_y) > 0:
        result['y'] = result_y
    if len(result_z) > 0:
        result['z'] = result_z
    return result


def cuboid_intersect_and_split_x(c1, c_list):
    # this is very complicated
    return



def intersect_and_split(c1, c2):
    intersect_result = cuboid_intersect(c1, c2)
    if len(intersect_result) == 0:
        return [c1, c2]
    return_list = [c1]
    temp_list = []
    if 'x' in intersect_result:
        # check if c1.min_x is between c2.min_x and c2.max_x
        # if so, need to split c2 by c1.min_x
        if c1.min_x >= c2.min_x and c1.min_x <= c2.max_x:
            c2_split = c2.split('x', c1.min_x)
            # if c1.max_x is also between c2.min_x and c2.max_x
            # need to split it again
            if c1.max_x >= c2.min_x and c1.max_x <= c2.max_x:       
                c2_2nd_split = c2_split[1].split('x', c1.max_x)
                temp_list = c2_split[0] + c2_2nd_split
            else:
                temp_list = c2_split
        # same for c1.max_x
        elif c1.max_x >= c2.min_x and c1.max_x <= c2.max_x:
            c2_split = c2.split('x', c1.max_x)
            temp_list = c2_split 
    


    return return_list + temp_list