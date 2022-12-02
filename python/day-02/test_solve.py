import solve
import utils


def test_tabulate_choices_empty():
    rounds = []

    my_score, opp_score = utils.tabulate_choices(rounds)

    assert opp_score == 0
    assert my_score == 0


def test_tablulate_choices_one_round():
    rounds = [
        "A X",
    ]

    opp_score, my_score = utils.tabulate_choices(rounds)

    assert opp_score == 1
    assert my_score == 1


def test_tablulate_choices_invalid_choice():
    rounds = [
        "A Q",
    ]

    opp_score, my_score = utils.tabulate_choices(rounds)

    assert opp_score == 1
    assert my_score == 0


def test_tablulate_choices_multi_round():
    rounds = [
        "A X",
        "A X",
        "B Y",
        "B Y",
        "A Y",
        "A X",
    ]

    opp_score, my_score = utils.tabulate_choices(rounds)

    assert opp_score == 8
    assert my_score == 9


def test_tabulate_wins_empty():
    rounds = []

    opp_score, my_score = utils.tabulate_wins(rounds)

    assert opp_score == 0
    assert my_score == 0


def test_tabulate_wins_player_win():
    rounds = [
        "A Y",
    ]

    opp_score, my_score = utils.tabulate_wins(rounds)

    assert opp_score == 0
    assert my_score == 6


def test_tabulate_wins_opponent_win():
    rounds = [
        "A Z",
    ]

    opp_score, my_score = utils.tabulate_wins(rounds)

    assert opp_score == 6
    assert my_score == 0


def test_tabulate_wins_draw():
    rounds = [
        "A X",
    ]

    opp_score, my_score = utils.tabulate_wins(rounds)

    assert opp_score == 3
    assert my_score == 3


def test_tabulate_wins_multi_rounds():
    rounds = [
        "A X",
        "A X",
        "B Y",
        "B Y",
        "A Y",
        "A X",
    ]

    opp_score, my_score = utils.tabulate_wins(rounds)

    assert opp_score == 15
    assert my_score == 21


def test_part_1_sample_input():
    input_data = [
        "A Y",
        "B X",
        "C Z",
    ]

    player_score = solve.part_1(input_data)

    assert player_score == 15
