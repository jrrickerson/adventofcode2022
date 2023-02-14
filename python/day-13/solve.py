from functools import cmp_to_key
import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    ordered_pairs = []
    for i in range(0, len(input_data), 2):
        left = utils.parse_packet(input_data[i].strip())
        right = utils.parse_packet(input_data[i + 1].strip())
        if -1 == utils.compare(left, right):
            ordered_pairs.append((i // 2) + 1)

    return sum(ordered_pairs)


def part_2(input_data):
    DIVIDER_PACKETS = [[[2]], [[6]]]
    packets = [utils.parse_packet(line) for line in input_data]

    packets = DIVIDER_PACKETS + packets
    packets.sort(key=cmp_to_key(utils.compare))

    divider_idx1 = packets.index(DIVIDER_PACKETS[0]) + 1
    divider_idx2 = packets.index(DIVIDER_PACKETS[1]) + 1

    decoder_key = divider_idx1 * divider_idx2
    return decoder_key


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
    print("Solving Puzzle for Day 13:", "https://adventofcode.com/2022/day/13")
    print(main("../puzzles/day-13.input"))
