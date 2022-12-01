import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    calories_list = utils.convert_int_list(input_data)
    parts = utils.partition_list(calories_list)
    calorie_sums = utils.sum_partitions(parts)

    return max(calorie_sums)


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
        "Solving Puzzle for Day 1:",
        "https://adventofcode.com/2022/day/1")
    print(main("../puzzles/day-01.input"))
