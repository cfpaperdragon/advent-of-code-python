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