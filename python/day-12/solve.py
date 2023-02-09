import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    grid = utils.generate_grid_map(input_data)
    start = utils.find_marker_point(grid, marker="S")
    end = utils.find_marker_point(grid, marker="E")

    utils.normalize_heightmap(grid, {start: "a", end: "z"})

    path = utils.find_shortest_path(grid, start, end)

    return len(path) - 1


def part_2(input_data):
    # Find the grid start and end points
    # Use the end point and do a breadth first search until
    # we find a cell that matches the required height.
    grid = utils.generate_grid_map(input_data)
    start = utils.find_marker_point(grid, marker="S")
    end = utils.find_marker_point(grid, marker="E")

    utils.normalize_heightmap(grid, {start: "a", end: "z"})

    path = utils.find_nearest_start_level(
        end, grid, start_level=grid[start[1]][start[0]]
    )
    return len(path) - 1


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
    print("Solving Puzzle for Day 12:", "https://adventofcode.com/2022/day/12")
    print(main("../puzzles/day-12.input"))
