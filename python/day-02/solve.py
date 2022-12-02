import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    opponent_score, player_score = 0, 0
    opponent, player = utils.tabulate_choices(input_data)
    opponent_score += opponent
    player_score += player
    opponent, player = utils.tabulate_wins(input_data)
    opponent_score += opponent
    player_score += player

    return player_score


def part_2(input_data):
    pass


def main(input_file):
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print(
        "Solving Puzzle for Day 2:",
        "https://adventofcode.com/2022/day/2")
    print(main("../puzzles/day-02.input"))
