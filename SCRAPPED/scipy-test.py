from test_model import optimize_winrate, test_model
from opponent_brain import opponent_moves
import numpy as np
from scipy.optimize import minimize

PLAYER_MAX_SCORE = 10
OPPONENT_MAX_SCORE = 10

def objective(player_moves):
    reshaped_moves = np.reshape(player_moves, (PLAYER_MAX_SCORE, OPPONENT_MAX_SCORE)).astype(int)
    return 1 - test_model(first_move=0, use_first_move=False, player_actions=reshaped_moves, opponent_actions=opponent_moves, player_score_start=0, opponent_score_start=0, player_max_score=PLAYER_MAX_SCORE, opponent_max_score=OPPONENT_MAX_SCORE, test_rounds=100000)

player_moves = np.full((PLAYER_MAX_SCORE * OPPONENT_MAX_SCORE), [1])

# show initial objective
print('Initial Objective: ' + str(objective(player_moves)))

# optimize
bounds = ((0, 11), ) * (PLAYER_MAX_SCORE * OPPONENT_MAX_SCORE)
solution = minimize(objective, player_moves, method='SLSQP', bounds=bounds)
new_moves = solution.x

print('End Objective: ' + str(objective(new_moves)))

print(new_moves)