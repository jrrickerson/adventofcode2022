import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    cycles = utils.expand_program(input_data)

    interesting_cycles = range(20, 221, 40)
    signal_strengths = []

    x_register = 1
    prev_cycle = 0
    for i in interesting_cycles:
        idx = i - 1
        x_register += sum([c[1] for c in cycles[prev_cycle:idx]])
        print(f"Cycle {i}, {cycles[idx]}, X = {x_register}")
        signal = (i) * x_register
        signal_strengths.append(signal)
        prev_cycle = idx

    return sum(signal_strengths)


def part_2(input_data):
    cycles = utils.expand_program(input_data)

    x_register = 1
    crt = []
    for pos, cycle in enumerate(cycles):
        column = pos % 40
        # See if we're drawing a position within the 3 pixel sprite
        if column - 1 <= x_register <= column + 1:
            crt.append(True)
        else:
            crt.append(False)
        x_register += cycle[1]

    screen = utils.format_crt_string(crt)
    return "\n" + screen


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
    print("Solving Puzzle for Day 10:", "https://adventofcode.com/2022/day/10")
    print(main("../puzzles/day-10.input"))
