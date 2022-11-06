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


def cuboid_intersect_x(c1, c2):
    return (c2.min_x >= c1.min_x and c2.min_x <= c1.max_x) or (c2.max_x >= c1.min_x and c2.max_x <= c1.max_x)

def cuboid_intersect_y(c1, c2):
    return (c2.min_y >= c1.min_y and c2.min_y <= c1.max_y) or (c2.max_y >= c1.min_y and c2.max_y <= c1.max_y)

def cuboid_intersect_z(c1, c2):
    return (c2.min_z >= c1.min_z and c2.min_z <= c1.max_z) or (c2.max_z >= c1.min_z and c2.max_z <= c1.max_z)

def cuboid_intersect(c1, c2):
    result = []
    if cuboid_intersect_x(c1, c2):
        result.append('x')
    if cuboid_intersect_y(c1, c2):
        result.append('y')
    if cuboid_intersect_z(c1, c2):
        result.append('z')
    return result