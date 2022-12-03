
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
    "A A": (3, 3),  # Draw
    "B B": (3, 3),  # Draw
    "C C": (3, 3),  # Draw
    "A B": (0, 6),  # Player win
    "B C": (0, 6),  # Player win
    "C A": (0, 6),  # Player win
    "A C": (6, 0),  # Opponent win
    "B A": (6, 0),  # Opponent win
    "C B": (6, 0),  # Opponent win
}

SHAPE_MAP = {
    "A": "R",
    "B": "P",
    "C": "S",
    "R": "A",
    "P": "B",
    "S": "C",
}

WINNING_SHAPES = {
    "R": "S",
    "S": "P",
    "P": "R",
}

LOSING_SHAPES = {
    "R": "P",
    "S": "R",
    "P": "S",
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


def generate_rounds(strategies):
    rounds = []
    for strat in strategies:
        opponent, result = strat.split()
        opp_shape = SHAPE_MAP.get(opponent)
        if result == "X":
            player_shape = WINNING_SHAPES.get(opp_shape)
        elif result == "Y":
            player_shape = opp_shape
        else:
            player_shape = LOSING_SHAPES.get(opp_shape)
        player = SHAPE_MAP.get(player_shape)
        rounds.append(f"{opponent} {player}")
    return rounds
