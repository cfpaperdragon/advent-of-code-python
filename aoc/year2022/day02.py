# aoc.year2022.day02

def get_score_matrix():
    """
    return a score matrix where getting
    score['Rock']['Paper'] = win
    score['Rock']['Rock'] = draw
    etc  
    """
    lose = 0
    draw = 3
    win = 6

    score = {}
    score['Rock'] = {}
    score['Rock']['Rock'] = draw
    score['Rock']['Paper'] = win
    score['Rock']['Scissors'] = lose
    score['Paper'] = {}
    score['Paper']['Rock'] = lose
    score['Paper']['Paper'] = draw
    score['Paper']['Scissors'] = win
    score['Scissors'] = {}
    score['Scissors']['Rock'] = win
    score['Scissors']['Paper'] = lose
    score['Scissors']['Scissors'] = draw
    return score
                        
def get_reverse_matrix():
    """
    return the move to get a result
    move['Rock']['X'] = 'Paper'
    """

    lose = 'X'
    draw = 'Y'
    win = 'Z'

    move = {}
    move['Rock'] = {}
    move['Rock'][draw] = 'Rock'
    move['Rock'][win] = 'Paper'
    move['Rock'][lose] = 'Scissors'
    move['Paper'] = {}
    move['Paper'][lose] = 'Rock'
    move['Paper'][draw] = 'Paper'
    move['Paper'][win] = 'Scissors'
    move['Scissors'] = {}
    move['Scissors'][win] = 'Rock'
    move['Scissors'][lose] = 'Paper'
    move['Scissors'][draw] = 'Scissors'
    return move

def calculate_score_part2(input):
    player1 = ['A', 'B', 'C']
    lose = 0
    draw = 3
    win = 6
    match_result = {'X':lose, 'Y':draw, 'Z':win}
    shape = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

    moves = input.strip().split(' ')
    player1_move = moves[0]
    result = moves[1]

    result_value = match_result[result]
    shape_value = 0
    # given player1 move and result, need to find the shape
    if player1_move == player1[shape['Rock']]:
        if result == 'X':
            shape_value = shape_scores['Scissors']
        elif result == 'Y':
            shape_value = shape_scores['Rock']
        elif result == 'Z':
            shape_value = shape_scores['Paper']

    elif player1_move == player1[shape['Paper']]:
        if result == 'X':
            shape_value = shape_scores['Rock']
        elif result == 'Y':
            shape_value = shape_scores['Paper']
        elif result == 'Z':
            shape_value = shape_scores['Scissors']

    elif player1_move == player1[shape['Scissors']]:
        if result == 'X':
            shape_value = shape_scores['Paper']
        elif result == 'Y':
            shape_value = shape_scores['Scissors']
        elif result == 'Z':
            shape_value = shape_scores['Rock']

    else:
        raise Exception("Invalid value for player 1")

    return shape_value + result_value


def calculate(input_list, function_calculate_score):
    score_dict = {} # save the value of the score per player1 player2 combination
    score_result_dict = {} # count how many of each combination there are

    for input in input_list:
        if input in score_dict.keys():
            score_result_dict[input] += 1
        else:
            score_value = function_calculate_score(input)
            score_dict[input] = score_value
            score_result_dict[input] = 1

    # final result
    final_score = 0
    for key in score_dict.keys():
        final_score += score_dict[key]*score_result_dict[key]
    return final_score


def calculate_part1(input_list):
    player1 = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
    player2 = {'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    score_matrix = get_score_matrix()

    result = 0
    for input in input_list:
        moves = input.strip().split(' ')
        player1_move = moves[0]
        player2_move = moves[1]
        result += score_matrix[player1[player1_move]][player2[player2_move]] + shape_scores[player2[player2_move]]
    return result
    

def calculate_part2(input_list):
    player1 = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    score_matrix = get_score_matrix()
    move_matrix = get_reverse_matrix()

    result = 0
    for input in input_list:
        moves = input.strip().split(' ')
        player1_move = moves[0]
        match_result = moves[1]
        player2_move = move_matrix[player1[player1_move]][match_result]
        result += score_matrix[player1[player1_move]][player2_move] + shape_scores[player2_move]
    return result