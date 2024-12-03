# aoc.year2024.day02

def process_input_list(input_list):
    report_list = []
    for line in input_list:
        line = line.strip()
        report = []
        line_split = line.split(" ")
        for level in line_split:
            report.append(int(level))
        report_list.append(report)
    return report_list

def is_report_safe(report):
    first_level = report[0]
    second_level = report[1]
    if first_level < second_level:
        # print("inc")
        inc = True
    elif first_level > second_level:
        # print("desc")
        inc = False
    else:
        return False
    
    previous_level = second_level
    for i in range(2, len(report)):
        # print(report[i])
        if inc:
            if previous_level < report[i]:
                if (report[i] - previous_level) in [1,2,3]:
                    previous_level = report[i]
                    continue
                else:
                    return False
            else:
                return False
        else:
            if previous_level > report[i]:
                if (previous_level - report[i]) in [1,2,3]:
                    previous_level = report[i]
                    continue
                else:
                    return False
            else:
                return False
    return True



def calculate_part1(input_list):
    reports = process_input_list(input_list)
    count_safe = 0
    print(reports)
    for r in reports:
        print(r)
        if is_report_safe(r):
            count_safe += 1
    return count_safe


def calculate_part2(input_list):   
    return 0