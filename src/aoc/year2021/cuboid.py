# aoc.year2021.cuboid

# using 2020-17 3d map as inspiration
# a cuboid is a 3 level dictionary
# cuboid[z][y][x] will give us the point (x, y, z)
# inside we will save a state 1 for on, 0 for off
# let's make it a class

class Cuboid:
    """ 
    Cuboid class.
    Internally it is a dictionary with other dictionaries.
    """

    # The init method or constructor
    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z, start_state):
        dict_z = dict()
        for z in range(min_z, max_z+1):
            dict_y = dict()
            for y in range(min_y, max_y+1):
                dict_x = dict()
                for x in range(min_x, max_x+1):
                    dict_x[x] = start_state
                dict_y[y] = dict_x
            dict_z[z] = dict_y
        self.dict = dict_z

    
    def get(self, x, y, z):
        if z in self.dict.keys():
            if y in self.dict[z].keys():
                if x in self.dict[z][y].keys():
                    return self.dict[z][y][x]
        return 0


    def count_state(self):
        """Counts the state of the cuboid.
        Counts the value of each vertice/position of the cuboid.
        """
        count = 0
        zkeys = list(self.dict.keys())
        ykeys = list(self.dict[zkeys[0]].keys())
        xkeys = list(self.dict[zkeys[0]][ykeys[0]].keys())
        for zkey in zkeys:
            for ykey in ykeys:
                for xkey in xkeys:
                    count += self.dict[zkey][ykey][xkey]
        return count
   

    def get_keys(self, axis, sort):
        """Gets keys for a particular axis of the cuboid.

        Parameters
        ----------
        cuboid : cuboid
        axis: 'x', 'y', 'z' or 'all'
        sort: True or False

        Returns
        A list containing the lists of keys (1 or all)
        """
        if axis not in ['x', 'y', 'z', 'all']:
            return []
        # z is the outmost dict
        zkeys = list(self.dict.keys())
        if sort:
            zkeys.sort()
        if axis == 'z':
            return [zkeys]
        # y is second level
        ykeys = list(self.dict[zkeys[0]].keys())
        if sort:
            ykeys.sort()
        if axis == 'y':
            return [ykeys]
        # x is the third level
        xkeys = list(self.dict[zkeys[0]][ykeys[0]].keys())
        if sort:
            xkeys.sort()
        if axis == 'x':
            return [xkeys]

        if axis == 'all':
            return [xkeys, ykeys, zkeys]


    def print(self):
        """Prints the cuboid.
        Prints a grid with each "slice" of z
        """
        all_keys = self.get_keys('all', True)
        xkeys = all_keys[0]
        ykeys = all_keys[1]
        zkeys = all_keys[2]
        for zkey in zkeys:
            print(f"z = {zkey}")
            for ykey in ykeys:
                line_string = ""
                for xkey in xkeys:
                    line_string += str(self.dict[zkey][ykey][xkey])
                print(line_string)


    def extend_z(self, new_z, value):
        """Adds the new_z to the tridimentional grid.
        """
        all_keys = self.get_keys('all', False)
        xkeys = all_keys[0]
        ykeys = all_keys[1]
        zkeys = all_keys[2]
        if new_z in zkeys:
            return # nothing to do
        new_dict_y = dict()
        for ykey in ykeys:
            new_dict_x = dict()
            for xkey in xkeys:
                new_dict_x[xkey] = value
            new_dict_y[ykey] = new_dict_x
        self.dict[new_z] = new_dict_y


    def extend_y(self, new_y, value):
        """Adds the new_y to the tridimentional grid.
        """
        xkeys = self.get_keys('x', False)[0]
        for zkey in self.dict.keys():
            new_dict_x = dict()
            for xkey in xkeys:
                new_dict_x[xkey] = value
            self.dict[zkey][new_y] = new_dict_x


    def extend_x(self, new_x, value):
        """Adds the new_x to the tridimentional grid.
        """
        for zkey in self.dict.keys():
            for ykey in self.dict[zkey].keys():
                self.dict[zkey][ykey][new_x] = value


    def set_simple(self, x, y, z, value):
        self.dict[z][y][x] = value

    
    def set_and_expand(self, x, y, z, expand_value, set_value):
        """Sets value in position (x,y,z)
        If the position doesn't exist yet in the cuboid, expand the cuboid.
        """
        xkeys = self.get_keys('x', False)[0]
        if x not in xkeys:
            self.extend_x(x, expand_value)

        ykeys = self.get_keys('y', False)[0]
        if y not in ykeys:
            self.extend_y(y, expand_value)

        zkeys = self.get_keys('z', False)[0]
        if z not in zkeys:
            self.extend_z(z, expand_value)

        self.set_simple(x, y, z, set_value)
