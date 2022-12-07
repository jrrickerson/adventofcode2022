import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    start = utils.find_set_span(input_data[0], size=4)
    return start + 4


def part_2(input_data):
    start = utils.find_set_span(input_data[0], size=14)
    return start + 14


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
    print("Solving Puzzle for Day 6:", "https://adventofcode.com/2022/day/6")
    print(main("../puzzles/day-06.input"))
