from test_model import get_turn_estimate

#from VERSION_0.brain_0 import moves as opponent_moves
#from brain import moves as player_moves
from VERSION_4.brain_4 import moves as opponent_moves
from VERSION_5.brain_5 import moves as player_moves

result = get_turn_estimate(player_moves, opponent_moves, test_rounds=10000000)

storage_file = open("time_trot_data.txt", "w")
storage_file.write("\n".join(str(i) for i in result))
storage_file.close()