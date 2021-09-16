from test_model import optimize_winrate, random_turn, get_best_turn, get_key
from opponent_brain import opponent_moves
#from player_moves_incomp import player_moves_incomplete

file_name = "player_moves_"
version = 0

PLAYER_MAX_SCORE = 50
OPPONENT_MAX_SCORE = 50

USING_INCOMPLETE_FILE = False
if USING_INCOMPLETE_FILE:
    player_moves = player_moves_incomplete
else:
    player_moves = [[{} for rows in range(PLAYER_MAX_SCORE)] for cols in range(OPPONENT_MAX_SCORE)]

#USING DEFAULT OPPONENT MOVES
opponent_moves = 0

counter = 0
for current_opponent_score in range(OPPONENT_MAX_SCORE - 1, -1, -1):
    for current_player_score in range(PLAYER_MAX_SCORE - 1, -1, -1):
        if len(player_moves[current_player_score][current_opponent_score]) == 0:
            player_moves = optimize_winrate(player_moves, opponent_moves, current_player_score, current_opponent_score, PLAYER_MAX_SCORE, OPPONENT_MAX_SCORE)
        counter += 1
        print("GAMESTATE:", counter)
        print("Weights:", player_moves[current_player_score][current_opponent_score])

    version += 1
    storage_file = open(file_name + str(version) + ".txt", "w")
    storage_file.write("\n".join(str(i) for i in player_moves))
    storage_file.close()