from dependencies import take_turn
import random
from time_trot_data.data_3 import trot
 
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

def train_model_against_random(first_move=0, player_actions=4, player_score_start=0, opponent_score_start=0, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    total_winrate = 0
    for _ in range(test_rounds):
        result_winrate = 0
        playerScore = player_score_start
        opponentScore = opponent_score_start

        current_turn = random_turn(player_score_start, opponent_score_start)

        take_extra_turn = False
        enable_time_trot = False

        player_move = first_move #Determine player move
        if current_turn != -1 and player_move == current_turn % 8:
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
            result_winrate = get_best_winrate(player_actions[playerScore][opponentScore])
        
        total_winrate += result_winrate

    return total_winrate / test_rounds

def train_model_against_opponent(first_move=0, player_actions=4, opponent_actions=4, player_score_start=0, opponent_score_start=0, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    total_winrate = 0
    for _ in range(test_rounds):
        result_winrate = 0
        playerScore = player_score_start
        opponentScore = opponent_score_start

        current_turn = random_turn(player_score_start, opponent_score_start)

        take_extra_turn = False
        enable_time_trot = True

        player_move = first_move #Determine player move
        if current_turn != -1 and player_move == current_turn % 8:
            take_extra_turn = True
        
        playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
        if current_turn != -1: current_turn += 1

        if take_extra_turn and not player_won and enable_time_trot: #Implemented only for player atm
            take_extra_turn = False
            player_move = get_best_turn(player_actions[playerScore][opponentScore])
            playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
            current_turn += 1

        if not player_won:
            #DETERMINE OPPONENT'S MOVE
            #opponent_move = opponent_actions[opponentScore][playerScore]
            if -1 < current_turn <= 12:
                opponent_move = current_turn % 8
                take_extra_turn = True
            else:
                opponent_move = noisy_move(opponent_actions[opponentScore][playerScore])
            #DETERMINE OPPONENT'S MOVE
            opponentScore, playerScore, opponent_won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)
            
            if take_extra_turn and not opponent_won and enable_time_trot: #Implemented only for player atm
                opponent_move = noisy_move(opponent_actions[opponentScore][playerScore])
                opponentScore, playerScore, opponent_won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)


        #Calculating resulting winrate of action
        if player_won:
            result_winrate = 1
        elif opponent_won:
            result_winrate = 0
        else:            
            result_winrate = get_best_winrate(player_actions[playerScore][opponentScore])
        
        total_winrate += result_winrate

    return total_winrate / test_rounds

def train_model_against_self(first_move, actions, player_score_start=0, opponent_score_start=0, test_rounds=100000):
    total_winrate = 0
    for _ in range(test_rounds):
        result_winrate = 0
        playerScore = player_score_start
        opponentScore = opponent_score_start
        current_turn = random_turn(player_score_start, opponent_score_start)

        take_extra_turn = False

        player_move = first_move #Determine player move
        if current_turn != -1 and player_move == current_turn % 8:
            take_extra_turn = True
        
        playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=50)
        if current_turn != -1: current_turn += 1

        if take_extra_turn and not player_won: #Implemented only for player atm
            take_extra_turn = False
            player_move = get_best_turn(actions[playerScore][opponentScore])
            playerScore, opponentScore, player_won = take_turn(playerScore, opponentScore, player_move, max_score=50)
            current_turn += 1

        if not player_won:
            #DETERMINE OPPONENT'S MOVE
            #if -1 < current_turn <= 12:
            #     opponent_move = current_turn % 8
            #     take_extra_turn = True
            # else:
            #     opponent_move = noisy_move(opponent_actions[opponentScore][playerScore])

            #Consider limiting perfect knowledge to max turn number
            if get_best_winrate(actions[opponentScore][playerScore]) == 1:
                opponent_move = get_best_turn(actions[opponentScore][playerScore])
            else:
                opponent_move = current_turn % 8
                take_extra_turn = True

            opponentScore, playerScore, opponent_won = take_turn(opponentScore, playerScore, opponent_move, max_score=50)
            
            if take_extra_turn and not opponent_won: #Implemented only for player atm
                opponent_move = noisy_move(actions[opponentScore][playerScore])
                opponentScore, playerScore, opponent_won = take_turn(opponentScore, playerScore, opponent_move, max_score=50)


        #Calculating resulting winrate of action
        if player_won:
            result_winrate = 1
        elif opponent_won:
            result_winrate = 0
        else:            
            result_winrate = get_best_winrate(actions[playerScore][opponentScore])
        
        total_winrate += result_winrate

    return total_winrate / test_rounds

def optimize_winrate(player_moves, player_score_start, opponent_score_start):

    if abs(player_score_start - opponent_score_start) > 30:
        test_rounds = 100000
    elif player_score_start < 35 and opponent_score_start < 35:
        test_rounds = 100000
    else:
        test_rounds = 100000

    for move in range(0, 11):
        #current_winrate = train_model_against_random(move, player_moves, player_score_start=player_score_start, opponent_score_start=opponent_score_start, player_max_score=player_max_score, opponent_max_score=opponent_max_score, test_rounds=test_rounds)
        current_winrate = train_model_against_self(move, player_moves, player_score_start=player_score_start, opponent_score_start=opponent_score_start, test_rounds=test_rounds)
        player_moves[player_score_start][opponent_score_start][move] = current_winrate

    if player_score_start != opponent_score_start: #Do other side of array if not corner
        for move in range(0, 11):
            current_winrate = train_model_against_self(move, player_moves, player_score_start=opponent_score_start, opponent_score_start=player_score_start, test_rounds=test_rounds)
            player_moves[opponent_score_start][player_score_start][move] = current_winrate

    return player_moves

def get_turn_estimate(player_actions=4, opponent_actions=4, player_max_score=50, opponent_max_score=50, test_rounds=100000):
    score_turn_average = [[{} for i in range(50)] for j in range(50)]

    for _ in range(test_rounds):
        playerScore = 0
        opponentScore = 0
        turn_counter = 0
        won = False
        got_time_trot = False
        while True:

            try:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
            try:
                score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] = 1

            if won:
                break

            #player_move = player_actions[playerScore][opponentScore]
            if turn_counter <= 12:
                player_move = turn_counter % 8
                got_time_trot = True
            else:
                player_move = noisy_move(player_actions[playerScore][opponentScore])
            playerScore, opponentScore, won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
            turn_counter += 1

            try:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
            try:
                score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] += 1
            except:
                score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] = 1
            
            if won:
                break

            #Extra turn from time_trot
            if got_time_trot:
                got_time_trot = False
                player_move = noisy_move(player_actions[playerScore][opponentScore])
                playerScore, opponentScore, won = take_turn(playerScore, opponentScore, player_move, max_score=player_max_score)
                turn_counter += 1

                try:
                    score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
                except:
                    score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
                try:
                    score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] += 1
                except:
                    score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] = 1

                if won:
                    break

            if turn_counter <= 12:
                opponent_move = turn_counter % 8
                got_time_trot = True
            else:
                opponent_move = noisy_move(opponent_actions[opponentScore][playerScore])
            opponentScore, playerScore, won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)
            turn_counter += 1

            if got_time_trot:
                got_time_trot = False
                try:
                    score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] += 1
                except:
                    score_turn_average[min(49, playerScore)][min(49, opponentScore)][turn_counter] = 1
                try:
                    score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] += 1
                except:
                    score_turn_average[min(49, opponentScore)][min(49, playerScore)][turn_counter] = 1

                if won:
                    break

                opponent_move = noisy_move(opponent_actions[opponentScore][playerScore])
                opponentScore, playerScore, won = take_turn(opponentScore, playerScore, opponent_move, max_score=opponent_max_score)
                turn_counter += 1

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

def noisy_move(moves): #Moves is a dict with 11 keys
    top_moves = {}
    best_move = get_best_turn(moves)
    top_moves[best_move] = moves[best_move]
    if moves[best_move] == 1:
        return best_move
    for i in moves:
        if i != best_move and moves[i] >= moves[best_move] - 0.05:
            top_moves[i] = moves[i]
    return list(top_moves.keys())[random.randint(0, len(top_moves.keys()) - 1)]

def get_key(dict, val):
    for i in dict:
        if dict[i] == val:
            return i

def get_best_turn(dict):
    return get_key(dict, max(dict.values()))

def get_best_winrate(dict):
    return max(dict.values())