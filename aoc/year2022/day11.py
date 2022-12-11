# aoc.year2022.day11

def parse_starting_items(string):
    if "Starting items" not in string:
        raise Exception("unexpected str: " + string)
    parts = string.split(':')
    parts_items = parts[1].strip().split(',')
    starting_items = []
    for item in parts_items:
        # print(item)
        starting_items.append(int(item.strip()))
    return starting_items

def parse_operation(string):
    if "Operation" not in string:
        raise Exception("unexpected str: " + string)
    parts = string.split(':')
    # print(parts[1])
    operation_str = parts[1]
    operation_str = operation_str.replace("new", "lambda a")
    operation_str = operation_str.replace("=", ":")
    operation_str = operation_str.replace("old", "a")
    # print(operation_str)
    operation = eval(operation_str)
    # print(operation)
    return operation

def parse_test(string):
    if "Test" not in string:
        raise Exception("unexpected str: " + string)
    parts = string.strip().split(' ')
    test = int(parts[3].strip())
    return test

def parse_test_result(string, result):
    if result not in string:
        raise Exception("unexpected str: " + string)
    parts = string.strip().split(' ')
    value = int(parts[5].strip())
    return value

def parse_input(input_list):

    monkeys = {}
    monkey_counter = 0

    while len(input_list) > 0:
        new_monkey = {}
        monkey_header = input_list.pop(0)
        if "Monkey" not in monkey_header:
            # something went wrong
            raise Exception("unexpected header: " + monkey_header)
        
        starting_items_str = input_list.pop(0)
        new_monkey["items"] = parse_starting_items(starting_items_str)

        operation_str = input_list.pop(0)
        new_monkey["operation"] = parse_operation(operation_str)

        test_str = input_list.pop(0)
        new_monkey["test"] = parse_test(test_str)

        test_true_str = input_list.pop(0)
        new_monkey["test_true"] = parse_test_result(test_true_str, "true")
        
        test_false_str = input_list.pop(0)
        new_monkey["test_false"] = parse_test_result(test_false_str, "false")

        # pop empty string
        if len(input_list) > 0:
            input_list.pop(0)

        # add the counter
        new_monkey["counter"] = 0

        monkeys[monkey_counter] = new_monkey
        monkey_counter += 1

    return monkeys

def do_round(monkey, monkeys, worry_function):
    while len(monkeys[monkey]["items"]) > 0:
        item = monkeys[monkey]["items"].pop(0)
        monkeys[monkey]["counter"] += 1
        monkey_inspect_item(item, monkey, monkeys, worry_function)

def monkey_inspect_item(item, monkey, monkeys, worry_function):
    inspected_item = monkeys[monkey]["operation"](item)
    bored_value = worry_function(inspected_item)
    test_result = bored_value % monkeys[monkey]["test"]
    if  test_result == 0:
        monkeys[monkeys[monkey]["test_true"]]["items"].append(bored_value)
    else:
        monkeys[monkeys[monkey]["test_false"]]["items"].append(bored_value)
    # print("monkey", monkey, "item", item, "inspected_item", inspected_item, "bored_value", bored_value, "test_result", test_result)

def find_monkey_business(monkeys, round_limit, worry_function):
    round_counter = 1
    while round_counter <= round_limit:
        round_counter += 1
        for monkey in monkeys.keys():
            do_round(monkey, monkeys, worry_function)

    counter_list = []
    for key in monkeys:
        counter_list.append(monkeys[key]["counter"])

    counter_list.sort(reverse=True)
    most1 = counter_list.pop(0)
    most2 = counter_list.pop(0)
    result = most1 * most2
    # print(result)
    return result

def calculate_part1(input_list):
    monkeys = parse_input(input_list)

    limit = 20
    worry_function = lambda a: a // 3
    return find_monkey_business(monkeys, limit, worry_function)

def calculate_part2(input_list):
    monkeys = parse_input(input_list)

    # https://www.reddit.com/r/adventofcode/comments/zih7gf/comment/izr7ucq/?utm_source=share&utm_medium=web2x&context=3
    # I was close, but didn't remember to try the module
    # also didn't understand why it worked
    super_modulo = 1
    for key in monkeys.keys():
        super_modulo *= monkeys[key]["test"]

    limit = 10000
    worry_function = lambda a: a % super_modulo
    return find_monkey_business(monkeys, limit, worry_function)
