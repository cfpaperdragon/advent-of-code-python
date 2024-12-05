# aoc.year2024.grid

class Grid2d:
    """ 
    Grid2d class.
    Internally it is a dictionary with another  dictionary.
    Lightly based on the cuboid from 2021.
    The Grid2d is fixed and doesn't grow. 
    I feel I am always making this class, maybe I should make a final good version?!
    """

    def __init__(self, data_str_list, len_x, len_y):
        self.min_x = 0
        self.min_y = 0
        self.max_x = len_x - 1
        self.max_y = len_y - 1
        dict_y = dict()
        for y in range(self.min_y, self.max_y+1):
            dict_x = dict()
            data_str = data_str_list[y].strip();
            for x in range(self.min_x, self.max_x+1):
                dict_x[x] = data_str[x]
            dict_y[y] = dict_x
        self.dict = dict_y

    def get(self, x, y):
        if y in self.dict.keys():
            if x in self.dict[y].keys():
                return self.dict[y][x]
        return "."

def this_is_a_method():
    return 0