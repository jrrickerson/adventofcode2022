import utils


def get_input_data(filename):  # pragma: no cover
    pass


def part_1(input_data):
    pass


def part_2(input_data):
    pass


def main(input_file):  # pragma: no cover
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":  # pragma: no cover
    print(
        "Solving Puzzle for Day 14:", "https://adventofcode.com/2022/day/14"
    )
    print(main("../puzzles/day-14.input"))
