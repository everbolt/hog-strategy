def test_model(player, opponent, test_rounds=10000):
    wins_player = 0
    wins_opponent = 0

    for _ in range(test_rounds):
        playerScore = 0
        opponentScore = 0
        while True:
            stateInitial_player = agent_player.get_state(playerScore, opponentScore)
            action_player, NOUSE = agent_player.get_action(stateInitial_player)

            finalMove_player = agent_player.process_action(action_player)

            playerScore, opponentScore, NOUSE, won, NOUSE = takeTurn(playerScore, opponentScore, finalMove_player)

            if won:
                wins_player += 1
                break
            
            stateInitial_opponent = agent_opponent.get_state(opponentScore, playerScore)
            action_opponent, NOUSE = agent_opponent.get_action(stateInitial_opponent)

            finalMove_opponent = agent_opponent.process_action(action_opponent)

            opponentScore, playerScore, NOUSE, won, NOUSE = takeTurn(opponentScore, playerScore, finalMove_opponent)

            if won:
                wins_opponent += 1
                break