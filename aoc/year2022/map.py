import sys
sys.path.insert(0, '../')

from aoc.year2021.cuboid import Cuboid

class Map2d:
    def __init__(self, min_x, max_x, min_y, max_y, start_value):
        self.map = Cuboid(min_x, max_x, min_y, max_y, 0, 0, start_value)

    def set(self, x, y, expand_value, set_value):
        self.map.set_and_expand(x, y, 0, expand_value, set_value)
    
    def print(self):
        all_keys = self.map.get_keys('all', True)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        y_keys.sort(reverse=True)
        for y in y_keys:
            string = "y=" + str(y) + " "
            for x in x_keys:
                string += str(self.map.get(x, y, 0))
            print(string)

    def print_asc(self):
        all_keys = self.map.get_keys('all', True)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        for y in y_keys:
            string = ""
            for x in x_keys:
                string += str(self.map.get(x, y, 0))
            print(string)
        
    def count(self, function):
        all_keys = self.map.get_keys('all', False)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        count = 0
        for y in y_keys:
            for x in x_keys:
                if function(self.map.get(x, y, 0)):
                    count += 1
        return count

    def max_value(self):
        all_keys = self.map.get_keys('all', False)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        max_list = []
        for y in y_keys:
            max_list.append(max(list(self.map.dict[0][y].values())))
        return max(max_list)

    def get(self, x, y):
        return self.map.get(x, y, 0)

    def find_in_map(self, function_value):
        all_keys = self.map.get_keys('all', False)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        for y in y_keys:
            for x in x_keys:
                if function_value(self.map.get(x, y, 0)):
                    return (x,y)
        return -1

    def find_all_in_map(self, function_value):
        all_keys = self.map.get_keys('all', False)
        x_keys = all_keys[0]
        y_keys = all_keys[1]
        result = []
        for y in y_keys:
            for x in x_keys:
                if function_value(self.map.get(x, y, 0)):
                    result.append((x,y))
        return result