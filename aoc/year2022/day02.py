# aoc.year2022.day02

def calculate_score(input):
    player1 = ['A', 'B', 'C']
    player2 = ['X', 'Y', 'Z']
    shape = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    lose = 0
    draw = 3
    win = 6

    moves = input.strip().split(' ')
    player1_move = moves[0]
    player2_move = moves[1]

    result = 0
    shape_value = 0
    # result for player 2
    if player1_move == player1[shape['Rock']]:
        if player2_move == player2[shape['Rock']]:
            shape_value = shape_scores['Rock']
            result = draw
        elif player2_move == player2[shape['Paper']]:
            shape_value = shape_scores['Paper']
            result = win
        elif player2_move == player2[shape['Scissors']]:
            shape_value = shape_scores['Scissors']
            result = lose
        else:
            raise Exception("Invalid value for player 2")

    elif player1_move == player1[shape['Paper']]:
        if player2_move == player2[shape['Rock']]:
            shape_value = shape_scores['Rock']
            result = lose
        elif player2_move == player2[shape['Paper']]:
            shape_value = shape_scores['Paper']
            result = draw
        elif player2_move == player2[shape['Scissors']]:
            shape_value = shape_scores['Scissors']
            result = win
        else:
            raise Exception("Invalid value for player 2")

    elif player1_move == player1[shape['Scissors']]:
        if player2_move == player2[shape['Rock']]:
            shape_value = shape_scores['Rock']
            result = win
        elif player2_move == player2[shape['Paper']]:
            shape_value = shape_scores['Paper']
            result = lose
        elif player2_move == player2[shape['Scissors']]:
            shape_value = shape_scores['Scissors']
            result = draw
        else:
            raise Exception("Invalid value for player 2")

    else:
        raise Exception("Invalid value for player 1")

    return shape_value + result
                         



def calculate_part1(input_list):


    score_dict = {} # save the value of the score per player1 player2 combination
    score_result_dict = {} # count how many of each combination there are

    for input in input_list:
        if input in score_dict.keys():
            score_result_dict[input] += 1
        else:
            score_value = calculate_score(input)
            score_dict[input] = score_value
            score_result_dict[input] = 1

    # final result
    final_score = 0
    for key in score_dict.keys():
        final_score += score_dict[key]*score_result_dict[key]
    return final_score

def calculate_part2(input_list):
    return 0
