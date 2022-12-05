import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    range_pairs = [utils.split_ranges(line) for line in input_data]

    complete_subsets = 0
    for pair in range_pairs:
        first = utils.generate_range_set(pair[0])
        second = utils.generate_range_set(pair[1])

        if first.issubset(second) or second.issubset(first):
            complete_subsets += 1
    return complete_subsets


def part_2(input_data):
    range_pairs = [utils.split_ranges(line) for line in input_data]

    overlaps = 0
    for pair in range_pairs:
        first = utils.generate_range_set(pair[0])
        second = utils.generate_range_set(pair[1])

        if set.intersection(first, second):
            overlaps += 1
    return overlaps


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
    print("Solving Puzzle for Day 4:", "https://adventofcode.com/2022/day/4")
    print(main("../puzzles/day-04.input"))
