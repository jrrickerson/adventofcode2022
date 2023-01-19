import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    # Start Head and Tail at origin point
    # Loop over commands, expanding them into individual "steps"
    # Move Head according to each step
    # After each step, update Tail position based on Head position
    # Record each tail position
    # Return count of unique positions
    ORIGIN = utils.Vector2d(0, 0)
    MAX_LEN = 1

    head = utils.Vector2d(ORIGIN.x, ORIGIN.y)
    tail = utils.Vector2d(ORIGIN.x, ORIGIN.y)

    tail_log = set()
    tail_log.add(tail)

    for motion in input_data:
        steps = utils.motion_to_steps(motion)
        for step in steps:
            head = utils.move_point(step, head)
            dist = utils.get_vector_distance(tail, head)
            # See if the head has moved far enough for the tail
            # to need to move
            if abs(dist.x) > MAX_LEN or abs(dist.y) > MAX_LEN:
                tail_step = utils.normalize_step(dist)
                tail = utils.move_point(tail_step, tail)
                tail_log.add(tail)

    return len(tail_log)


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
    print("Solving Puzzle for Day 9:", "https://adventofcode.com/2022/day/9")
    print(main("../puzzles/day-09.input"))
