# aoc.year2024.day05

def process_input_list(input_list):
    rules_dict = {}
    # start_node_rules = Cache()
    # end_node_rules = Cache()
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
        rule = (start_node, end_node)
        rules_dict[rule] = True
        # start_node_rules.add(rule)
        # end_node_rules.add(rule)
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
    return rules_dict, print_lists


def calculate_part1(input_list):
    # within each update, the ordering rules that involve missing page numbers are not used
    # do I need to calculate the graph for each update?
    rules_dict, print_lists = process_input_list(input_list)
    # what if I don't need to create a graph?
    result, _ = classify_lists(print_lists, rules_dict)
    return result


def classify_lists(print_lists, rules_dict):
    mid_page_sum = 0
    bad_list = []
    for print_list in print_lists:
        good_list = True
        for i in range(1, len(print_list)):
            previous_page = print_list[i-1]
            page = print_list[i]
            # we have (previous_page, page) pair
            # search for a rule that breaks that pair (page, previous_page)
            if (page, previous_page) in rules_dict.keys():
                good_list = False
                break
        if good_list:
            mid_page_index = len(print_list) // 2
            mid_page_sum += print_list[mid_page_index]
        else:
            bad_list.append(print_list)
    return mid_page_sum, bad_list


def calculate_part2(input_list):  
    # within each update, the ordering rules that involve missing page numbers are not used
    # do I need to calculate the graph for each update?
    rules_dict, print_lists = process_input_list(input_list)
    # what if I don't need to create a graph?
    _, incorrect_list = classify_lists(print_lists, rules_dict)
    return 0
