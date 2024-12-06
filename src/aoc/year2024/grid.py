# aoc.year2024.grid

class Grid2d:
    """ 
    Grid2d class.
    Internally it is a dictionary with another  dictionary.
    Lightly based on the cuboid from 2021.
    The Grid2d is fixed and doesn't grow. 
    I feel I am always making this class, maybe I should make a final good version?!
    """

    def __init__(self, data_str_list, len_x, len_y, find_character = False, character = ""):
        self.min_x = 0
        self.min_y = 0
        self.max_x = len_x - 1
        self.max_y = len_y - 1
        self.character_pos = (0, 0)
        dict_y = dict()
        for y in range(self.min_y, self.max_y+1):
            dict_x = dict()
            data_str = data_str_list[y].strip();
            for x in range(self.min_x, self.max_x+1):
                dict_x[x] = data_str[x]
                if find_character:
                    if data_str[x] == character:
                        self.character_pos = (x, y)
            dict_y[y] = dict_x
        self.dict = dict_y

    def get(self, x, y):
        if y in self.dict.keys():
            if x in self.dict[y].keys():
                return self.dict[y][x]
        return "."
    
    def set(self, x, y, value):
        if y in self.dict.keys():
            if x in self.dict[y].keys():
                self.dict[y][x] = value

    def count_value(self, value):
        count = 0
        for y in self.dict.keys():
            for x in self.dict[y].keys():
                if self.dict[y][x] == value:
                    count += 1
        return count
    
    def print(self):
        for y in range(self.min_y, self.max_y + 1):
            line = ""
            for x in range(self.min_x, self.max_x + 1):
                line += self.get(x, y)
            print(line)

def this_is_a_method():
    return 0