
RPS_CHOICE_SCORE = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

WIN_LOSE_DRAW_SCORE = {
    "A X": (3, 3),  # Draw
    "B Y": (3, 3),  # Draw
    "C Z": (3, 3),  # Draw
    "A Y": (0, 6),  # Player win
    "B Z": (0, 6),  # Player win
    "C X": (0, 6),  # Player win
    "A Z": (6, 0),  # Opponent win
    "B X": (6, 0),  # Opponent win
    "C Y": (6, 0),  # Opponent win
}


def tabulate_choices(rounds):
    """Given a list of string representing Rock, Paper, Scissors
    rounds, tabulate the score for the opponents' choice vs. the player's
    choice of play.
    Rock = 1, Paper = 2, Scissors = 3
    NOTE: This does not determine a winner or award points for winning."""

    player_score, opp_score = 0, 0

    for round in rounds:
        opponent, player = round.split()
        opp_score += RPS_CHOICE_SCORE.get(opponent, 0)
        player_score += RPS_CHOICE_SCORE.get(player, 0)

    return opp_score, player_score


def tabulate_wins(rounds):
    """Given a list of strings representing Rock, Paper, Scissors
    rounds, tabulate the score for which player won the round.
    Win = 6, Draw = 3, Loss = 0"""

    player_score, opp_score = 0, 0
    for round in rounds:
        opp, player = WIN_LOSE_DRAW_SCORE.get(round, (0, 0))
        opp_score += opp
        player_score += player

    return opp_score, player_score

