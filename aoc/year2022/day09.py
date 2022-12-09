# aoc.year2022.day09

from aoc.year2022.map import Map2d as Map2d

def move_all(map, head_position, tail_position, direction, amount):
    while amount > 0:
        amount -= 1
        head_position, tail_position = move_one(map, head_position, tail_position, direction)
    return head_position, tail_position

def move_head_one(head, direction):
    if direction == 'R':
        # x +1
        new_nead = (head[0]+1, head[1])
    elif direction == 'L':
        # x -1
        new_nead = (head[0]-1, head[1])
    elif direction == 'U':
        # y +1
        new_nead = (head[0], head[1]+1)
    elif direction == 'D':
        # y -1
        new_nead = (head[0], head[1]-1)
    else:
        raise Exception("invalid direction: " + direction)
    return new_nead

def move_tail_if_needed(head, tail):
    new_tail_x = tail[0]
    new_tail_y = tail[1]

    # same x and same y
    if head[0] == tail[0] and head[1] == tail[1]:
        return tail

    # in same x
    elif head[0] == tail[0]:
        if head[1] > tail[1]:
            if head[1] - tail[1] > 1:
                new_tail_y += 1
        elif head[1] < tail[1]:
            if tail[1] - head[1] > 1:
                new_tail_y -= 1
    # in same y
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            if head[0] - tail[0] > 1:
                new_tail_x += 1
        elif head[0] < tail[0]:
            if tail[0] - head[0] > 1:
                new_tail_x -= 1 
    
    # not in same x nor y
    elif head[0] != tail[0] and head[1] != tail[1]:
        # print(head, tail)
        # but are they adjacent?
        # if head = (0,0)
        # tail is adjacent/diagonal if (1,1), (1,-1), (-1,1), (-1,-1)
        if head[0] > tail[0] and head[1] > tail[1]:
            # print("zone 1")
            if head[0] - tail[0] > 1 or head[1] - tail[1] > 1:
                # print("zone 1 - not adjacent")
                new_tail_x += 1
                new_tail_y += 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            # print("zone 2")
            if head[0] - tail[0] > 1 or tail[1] - head[1] > 1:
                # print("zone 2 - not adjacent")
                new_tail_x += 1
                new_tail_y -= 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            # print("zone 3")
            if tail[0] - head[0] > 1 or tail[1] - head[1] > 1:
                # print("zone 3 - not adjacent")
                new_tail_x -= 1
                new_tail_y -= 1
        elif head[0] < tail[0] and head[1] > tail[1]:
            # print("zone 4")
            if tail[0] - head[0] > 1 or head[1] - tail[1] > 1:
                # print("zone 4 - not adjacent")
                new_tail_x -= 1
                new_tail_y += 1    
    return (new_tail_x, new_tail_y)                                  

def move_one(map, head, tail, direction):
    # the head always moves
    new_head = move_head_one(head, direction)
    # the tail may move
    new_tail = move_tail_if_needed(new_head, tail)
    # print("head", head, "new_head", new_head, "tail", tail, "new_tail", new_tail)
    if tail != new_tail:
        map.set(new_tail[0], new_tail[1], '.', '#')        
    return new_head, new_tail


def calculate_part1(input_list):
    rope_map = Map2d(0, 10, 0, 10, '.')

    start = (0, 0)
    tail = start
    head = start
    
    for input in input_list:
        # parse input
        parts = input.split(' ')
        direction = parts[0]
        amount = int(parts[1])
        # print(direction, amount)
        head, tail = move_all(rope_map, head, tail, direction, amount)
    # rope_map.print()
    rope_map.set(0, 0, ".", "#") # make sure start position is marked

    result = rope_map.count(lambda a: a == '#')
    return result

def calculate_part2(input_list):
    return 0
