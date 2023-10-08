# aoc.year2022.day15

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
def process_line(line):
    parts = line.split(' ')

    sensor_x_str = parts[2]
    sensor_x = int(sensor_x_str[2:-1])
    sensor_y_str = parts[3]
    sensor_y = int(sensor_y_str[2:-1])

    beacon_x_str = parts[8]
    beacon_x = int(beacon_x_str[2:-1])
    beacon_y_str = parts[9]
    beacon_y = int(beacon_y_str[2:])
    
    return (sensor_x, sensor_y), (beacon_x, beacon_y)

def calculate_part1(input_list, y_line):

    sensor_beacon_pairs = []
    for input in input_list:
        sensor, beacon = process_line(input)
        sensor_beacon_pairs.append((sensor, beacon))

    # need to check if the circle with sensor as center, and radius the vector "sensor-beacon" intersects line Y=YLINE

    cross_pairs_and_md = []
    for sbp in sensor_beacon_pairs:
        s = sbp[0]
        b = sbp[1]
        md = abs(s[0]-b[0]) + abs(s[1]-b[1])
        if s[1] < y_line:
            if s[1] + md > y_line:
                # print(sbp, "crosses line", y_line, "distance", md)
                cross_pairs_and_md.append((sbp[0], sbp[1], md))
        elif s[1] > y_line:
            if s[1] - md < y_line:
                # print(sbp, "crosses line", y_line, "distance", md)
                cross_pairs_and_md.append((sbp[0], sbp[1], md))
        else: # s[1] == y_line
            # print(sbp, "crosses line", y_line, "distance", md)
            cross_pairs_and_md.append((sbp[0], sbp[1], md))

    intersect_x = []
    for cp in cross_pairs_and_md:
        s = cp[0]
        b = cp[1]
        md = cp[2]

        px_1 = - (md - abs(y_line - s[1])) + s[0]
        px_2 = (md - abs(y_line - s[1])) + s[0]
        intersect_x.append(px_1)
        intersect_x.append(px_2)
        
    intersect_x.sort()
    # print(intersect_x)
    min_x = intersect_x[0]
    max_x = intersect_x[-1]

    beacons_in_y_line = []
    for sbp in sensor_beacon_pairs:
        b = sbp[1]
        if b[1] == y_line:
            if b[0] not in beacons_in_y_line:
                beacons_in_y_line.append(b[0])
    result = abs(min_x) + abs(max_x) + 1 - len(beacons_in_y_line)
    return result

def calculate_part2(input_list):
    return 0
