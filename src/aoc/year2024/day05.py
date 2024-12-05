# aoc.year2024.day05
from aoc.year2024.graph import DirectedGraph as Graph

def process_input_list(input_list):
    graph = Graph()
    print_lists = []
    i = 0
    size = len(input_list)
    # parse page ordering rules
    while i < size:
        input_str = input_list[i].strip()
        if len(input_str) == 0: # reached the separator line
            break
        split_input_str = input_str.split("|")
        start_node = int(split_input_str[0])
        end_node = int(split_input_str[1])
        graph.add_path(start_node, end_node)
        i += 1
    # separator
    i += 1
    # parse pages to produce in each update
    while i < size:
        input_str = input_list[i].strip()
        split_input_str = input_str.split(",")
        update_list = []
        for splitted in split_input_str:
            value = int(splitted)
            update_list.append(value)
        i += 1
        print_lists.append(update_list)
    return graph, print_lists


def traverse(graph, start_node, target_node, cache):  
    # first check the cache
    if (start_node, target_node) in cache.keys():
        return cache[(start_node, target_node)], cache
    # get the out nodes
    # if target_node in the out nodes, update cache and return true
    # else check each of the out nodes out nodes - recursively
    out_nodes = graph.get_out_nodes(start_node)
    if len(out_nodes) == 0:
        cache[(start_node, target_node)] = False
        return False, cache
    elif target_node in out_nodes:
        cache[(start_node, target_node)] = True
        return True, cache
    else:
        result = False
        for node in out_nodes:
            partial_result, cache = traverse(graph, node, target_node, cache)
            result = result or partial_result
            if result:
                cache[(start_node, target_node)] = True
                return result, cache # true, break
    cache[(start_node, target_node)] = False
    return result, cache # false, after traversing everything


def calculate_part1(input_list):
    # within each update, the ordering rules that involve missing page numbers are not used
    # do I need to calculate the graph for each update?
    graph, print_lists = process_input_list(input_list)
    graph.print()
    cache = {}
    middle_page_number_sum = 0
    for print_list in print_lists:
        result = True
        for i in range(1, len(print_list)):
            partial_result, cache = traverse(graph, print_list[i-1], print_list[i], cache)
            result = result and partial_result
            if not result:
                break # this list is not correct
        if result:
            print(print_list)
            middle_page_index = len(print_list) // 2
            middle_page_number_sum += print_list[middle_page_index]
    return middle_page_number_sum


def calculate_part2(input_list):  
    return 0
