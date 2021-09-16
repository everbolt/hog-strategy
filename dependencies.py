import numpy as np

def six_sided():
    return np.random.randint(1, 7)

def roll_dice(num_rolls, dice=six_sided):
    total = 0
    for _ in range(num_rolls):
        current_roll = dice()
        if current_roll == 1:
            return 1
        total += current_roll
    return total


#If player rolls 0, scores the nth decimal place of 1/7
#Where n is opponent's score
def picky_piggy(score):
    reduced_score = score % 6
    if not reduced_score:
        return 7
    picky_options = 758241
    return picky_options % (10 ** reduced_score) // (10 ** (reduced_score - 1))


#If player ends turn with matching score to opponent, player score doubles
def hog_pile(player_score, opponent_score):
    if player_score == opponent_score:
        return player_score
    return 0


#Returns new scores after 1 turn is taken given number of rolls
def take_turn(playerScore, opponentScore, num_rolls, dice=six_sided, max_score=50):

    if not num_rolls:
        playerScore += picky_piggy(opponentScore)
    else:
        playerScore += roll_dice(num_rolls)
    
    playerScore += hog_pile(playerScore, opponentScore)

    if playerScore >= max_score:
        won = True
    else:
        won = False

    return playerScore, opponentScore, won