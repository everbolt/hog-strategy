from dependencies import take_turn
import random
from time_trot import trot

def test_model(first_move=0, use_first_move=False, player_actions=4, opponent_actions=4, player_score_start=0, opponent_score_start=0, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    wins_player = 0
    wins_opponent = 0
    for _ in range(test_rounds):
        playerScore = player_score_start
        opponentScore = opponent_score_start

        if player_score_start == 0 and opponent_score_start == 0:
            turn_counter = 0
        else:
            turn_counter = random_turn(player_score_start, opponent_score_start)
        first_turn = True
        take_extra_turn = False
        unknown_first_turn = turn_counter == -1
        enable_time_trot = False
        while True:
            if first_turn and use_first_move:
                first_turn = False
                player_move = first_move
            else:
                player_move = get_best_turn(player_actions[playerScore][opponentScore])
                if player_move == -1: print("ERROR, move is -1")
            
            if player_move == turn_counter and not unknown_first_turn:
                take_extra_turn = True
            
            playerScore, opponentScore, won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
            turn_counter += 1

            if take_extra_turn and not won and enable_time_trot: #Implemented only for player atm
                take_extra_turn = False
                player_move = get_best_turn(player_actions[playerScore][opponentScore])
                playerScore, opponentScore, won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
                turn_counter += 1

            if won:
                wins_player += 1
                break
            
            #DETERMINE OPPONENT'S MOVE
            #opponent_move = opponent_actions[opponentScore][playerScore]
            opponent_move = random.randint(4,6)
            #DETERMINE OPPONENT'S MOVE

            opponentScore, playerScore, won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)
            turn_counter += 1

            if won:
                wins_opponent += 1
                break

    return wins_player / test_rounds

def test_model_v2(first_move=0, player_actions=4, opponent_actions=4, player_score_start=0, opponent_score_start=0, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    total_winrate = 0
    for _ in range(test_rounds):
        result_winrate = 0
        playerScore = player_score_start
        opponentScore = opponent_score_start

        current_turn = random_turn(player_score_start, opponent_score_start)
        unknown_first_turn = current_turn == -1

        take_extra_turn = False
        enable_time_trot = True

        player_move = first_move #Determine player move
        if player_move == current_turn and not unknown_first_turn:
            take_extra_turn = True
        
        playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)

        if take_extra_turn and not player_won and enable_time_trot: #Implemented only for player atm
            player_move = get_best_turn(player_actions[playerScore][opponentScore])
            playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)

        if not player_won:
            #DETERMINE OPPONENT'S MOVE
            #opponent_move = opponent_actions[opponentScore][playerScore]
            opponent_move = random.randint(4,6)
            #DETERMINE OPPONENT'S MOVE

            opponentScore, playerScore, opponent_won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)

        #Calculating resulting winrate of action
        if player_won:
            result_winrate = 1
        elif opponent_won:
            result_winrate = 0
        else:
            if playerScore > 49 or opponentScore > 49:
                print("Player score too high")
            
            result_winrate = get_best_winrate(player_actions[playerScore][opponentScore])
        
        total_winrate += result_winrate

    return total_winrate / test_rounds

def optimize_winrate(player_moves, opponent_moves, player_score_start, opponent_score_start, player_max_score, opponent_max_score):

    if abs(player_score_start - opponent_score_start) > 30:
        test_rounds = 10000
    elif player_score_start < 35 and opponent_score_start < 35:
        test_rounds = 100000
    else:
        test_rounds = 10000

    for move in range(0, 11):
        current_winrate = test_model_v2(move, player_moves, opponent_actions=opponent_moves, player_score_start=player_score_start, opponent_score_start=opponent_score_start, player_max_score=player_max_score, opponent_max_score=opponent_max_score, test_rounds=test_rounds)
        player_moves[player_score_start][opponent_score_start][move] = current_winrate

    return player_moves

def get_turn_estimate(player_actions=4, opponent_actions=4, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    wins_player = 0
    wins_opponent = 0

    score_turn_average = [[{} for i in range(50)] for j in range(50)]

    for _ in range(test_rounds):
        playerScore = 0
        opponentScore = 0
        turn_counter = 0
        won = False
        while True:

            try:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
            turn_counter += 1

            if won:
                wins_opponent += 1
                break

            player_move = player_actions[playerScore][opponentScore]
            playerScore, opponentScore, won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
            if won:
                wins_player += 1
                break

            try:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
            turn_counter += 1

            opponent_move = opponent_actions[opponentScore][playerScore]
            opponentScore, playerScore, won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)
        
        if _ % 100000 == 0:
            print("Game:", _)
    return score_turn_average

def random_turn(player_score, opponent_score):
    if not len(trot[player_score][opponent_score]):
        return -1
    elif sum(trot[player_score][opponent_score].values()) < 200:
        return -1
    
    random_value = random.randint(1, sum(trot[player_score][opponent_score].values()))
    selected_turn = -1
    while random_value > 0:
        selected_turn += 1
        try:
            random_value -= trot[player_score][opponent_score][selected_turn]
        except:
            pass
    return selected_turn

def get_key(dict, val):
    for i in dict:
        if dict[i] == val:
            return i

def get_best_turn(dict):
    return get_key(dict, max(dict.values()))

def get_best_winrate(dict):
    return max(dict.values())