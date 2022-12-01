import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    # Convert string input to integers
    calories_list = utils.convert_int_list(input_data)
    # Partition calorie groups per elf using blank line separators from input
    parts = utils.partition_list(calories_list)
    # Sum each individual elf's calorie list
    calorie_sums = utils.sum_partitions(parts)

    return max(calorie_sums)


def part_2(input_data):
    # Convert string input to integers
    calories_list = utils.convert_int_list(input_data)
    # Partition calorie groups per elf using blank line separators from input
    parts = utils.partition_list(calories_list)
    # Sum each individual elf's calorie list
    calorie_sums = utils.sum_partitions(parts)

    # Sort calorie sums descending and get the top three sums
    calorie_sums.sort(reverse=True)
    top_three = calorie_sums[:3]

    return sum(top_three)


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
