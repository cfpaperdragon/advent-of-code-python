# aoc.year2022.day07

i_type = 0
i_parent = 1
i_size = 2
i_list = 3


def build_dir_tree(input_list):
    """
    tree is a dict
    each node:
    * dir: <name> = (d, parent_dir, <size>, <list of nodes inside>)
    * file: <name> = (f, parent_dir, <size>)
    """
    # tree
    tree = {}
    root = '/'
    current_dir = root
    tree[root] = ('d', None, 0, [])

    for input in input_list:
        to_print = input
        parts = input.split(' ')
        if '$' in input: # it is a command
            if parts[1] == 'cd':
                if parts[2] == "..":
                    to_print += ' # move up a dir'
                    # move up a dir
                    if current_dir == root:
                        raise Exception("Can't move up from root!")
                    current_dir = tree[current_dir][i_parent]
                else:
                    to_print += ' # move into a dir'
                    # move into a dir
                    if parts[2] == root:
                        # don't need to do anything, this is the initial state
                        continue
                    else:
                        # can only move to a dir that is below the current_dir
                        # new_dir = parts[2]
                        new_dir = current_dir + "/" + parts[2]
                        if new_dir not in tree[current_dir][i_list]:
                            raise Exception("Can't move to dir " + new_dir + " from " + current_dir)
                        else:
                            current_dir = new_dir
            elif parts[1] == 'ls':
                to_print += ' # list dir'
                # current_dir should be a dir otherwise it will bork
                if tree[current_dir][i_type] != 'd':
                    raise Exception('Invalid ls: ' + current_dir + ' is not a dir.')
            else:
                raise Exception('Invalid Command: ' + parts[1])
        else:
            name = parts[1]
            fullpath = current_dir + "/" + name
            if parts[0] == 'dir':
                to_print += ' # it is a dir'
                size = 0
                # new node in the tree
                tree[fullpath] = ('d', current_dir, size, [])
            else: 
                to_print += ' # it is a file'
                size = int(parts[0])
                # new node in the tree
                tree[fullpath] = ('f', current_dir, size)
            # need to add it to the current_dir
            current = tree[current_dir]
            file_list = current[i_list]
            file_list.append(fullpath)
            tree[current_dir] = (current[i_type], current[i_parent], current[i_size], file_list)
        # print(to_print)
    # print(tree)

    return tree, root

def print_tree(tree):
    for key in tree:
        print(f"{key}: {tree[key]}")

def calculate_dir_size(tree, dir):

    dir_node = tree[dir]
    if dir_node[i_type] == 'f':
        return dir_node[i_size]
    if dir_node[i_size] != 0:
        return dir_node[i_size]
    size = 0
    for sub_node in dir_node[i_list]:
        node = tree[sub_node]
        if node[i_size] != 0:
            size += node[i_size]
        else:
            size += calculate_dir_size(tree, sub_node)
    # update size
    tree[dir] = (dir_node[i_type], dir_node[i_parent], size, dir_node[i_list])
    return size


def calculate_part1(input_list):
    
    tree, root = build_dir_tree(input_list)
    calculate_dir_size(tree, root)

    result = 0
    for key in tree.keys():
        node = tree[key]
        if node[i_type] == 'd':
            if node[i_size] <= 100000:
                result += node[i_size]
    return result

def calculate_part2(input_list):
    return 0

