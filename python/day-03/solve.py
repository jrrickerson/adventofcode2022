import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    all_priorities = []
    for line in input_data:
        parts = utils.split_into(line, parts=2)
        common_letters = utils.intersect_letters(parts)
        priorities = utils.map_priorities(common_letters)
        all_priorities += priorities
    return sum(all_priorities)


def part_2(input_data):
    group_size = 3
    all_priorities = []
    for idx in range(0, len(input_data), group_size):
        group = input_data[idx : idx + group_size]
        badge_letter = utils.intersect_letters(group)
        priorities = utils.map_priorities(badge_letter)
        all_priorities += priorities
    return sum(all_priorities)


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
    print("Solving Puzzle for Day 3:", "https://adventofcode.com/2022/day/3")
    print(main("../puzzles/day-03.input"))
