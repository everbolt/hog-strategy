#from brain import moves
from VERSION_4.brain_4 import moves
"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = 'computer go brrrr'  # Change this line!


def final_strategy(score, opponent_score):
    if not opponent_score:
        return 0
    if not score:
        return 1
    if score + opponent_score == 2 or score + opponent_score == 3:
        return 2
    return get_best_turn(moves[min(score, 49)][min(opponent_score, 49)])

def get_key(dict, val):
    for i in dict:
        if dict[i] == val:
            return i

def get_best_turn(dict):
    return get_key(dict, max(dict.values()))