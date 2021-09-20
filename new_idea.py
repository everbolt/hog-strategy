from test_model import optimize_winrate, random_turn, get_best_turn, get_key
from VERSION_6.brain_6 import moves as opponent_moves
#from player_moves_incomp import player_moves_incomplete

file_name = "player_moves_"
version = 0

MAX_SCORE = 50

# USING_INCOMPLETE_FILE = False
# if USING_INCOMPLETE_FILE:
#     player_moves = player_moves_incomplete

player_moves = [[{} for rows in range(MAX_SCORE)] for cols in range(MAX_SCORE)]

#USING DEFAULT OPPONENT MOVES
#opponent_moves = 0

counter = 0
for long_iter in range(MAX_SCORE - 1, -1, -1):
    for short_iter in range(long_iter, -1, -1):
        if len(player_moves[short_iter][long_iter]) == 0:
            player_moves = optimize_winrate(player_moves, short_iter, long_iter)
        counter += 1
        print("GAMESTATE:", counter)
        #print("Weights:", player_moves[current_player_score][current_opponent_score])

    version += 1
    storage_file = open(file_name + str(version) + ".txt", "w")
    storage_file.write("\n".join(str(i) for i in player_moves))
    storage_file.close()

#TODO:
#VARY THE FOLLOWING
# Noisy move percent
# Extent of opponent perfect knowledge
# Winrate minimum for opponent 1st move to override time trot