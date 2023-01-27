import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    monkeys = []
    lines = []
    for line in input_data:
        if not line.strip():
            monkeys.append(utils.parse_monkey(lines))
            lines.clear()
            continue
        lines.append(line)
    # Get the last monkey
    monkeys.append(utils.parse_monkey(lines))

    inspections = [0] * len(monkeys)
    for round in range(20):
        #print("=" * 30, "ROUND", round, "=" * 30)
        for i, monkey in enumerate(monkeys):
            inspected = utils.take_turn(monkey, monkeys)
            inspections[i] += inspected

    active_monkeys = sorted(inspections, reverse=True)
    #print(active_monkeys)
    return active_monkeys[0] * active_monkeys[1]



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
        "Solving Puzzle for Day 11:",
        "https://adventofcode.com/2022/day/11")
    print(main("../puzzles/day-11.input"))
