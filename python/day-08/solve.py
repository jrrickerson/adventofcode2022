import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    # Generate a grid from the input
    # For each row, detect visible trees
    # Add visible trees to set of visible
    # For each column, detect visible trees
    # Add visible trees to set of visible
    # Get the count of the visible set
    visible_trees = set()
    tree_grid = utils.generate_grid(input_data)
    # Add all the outside trees

    # Look at the inner trees by row
    for i, row in enumerate(tree_grid):
        visible = utils.find_visible(row)
        visible_trees |= utils.vectors_from_index_set(visible, row=i)

    # Look at the inner trees by column
    for i in range(len(tree_grid[0])):
        col = [row[i] for row in tree_grid]
        visible = utils.find_visible(col)
        visible_trees |= utils.vectors_from_index_set(visible, col=i)


    return len(visible_trees)


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
        "Solving Puzzle for Day 8:",
        "https://adventofcode.com/2022/day/8")
    print(main("../puzzles/day-08.input"))
