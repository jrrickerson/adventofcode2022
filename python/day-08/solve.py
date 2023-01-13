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

    # Look at the trees by row
    for i, row in enumerate(tree_grid):
        visible = utils.find_visible(row)
        visible_trees |= utils.vectors_from_index_set(visible, row=i)

    # Look at the trees by column
    for i in range(len(tree_grid[0])):
        col = [row[i] for row in tree_grid]
        visible = utils.find_visible(col)
        visible_trees |= utils.vectors_from_index_set(visible, col=i)


    return len(visible_trees)


def part_2(input_data):
    # Generate a grid of trees
    # Iterate over rows and columns, ignoring edges
    # For each tree, calculate scenic score
    # Return max score
    tree_grid = utils.generate_grid(input_data)
    num_rows = len(tree_grid)
    num_cols = len(tree_grid[0])

    max_scenic_score = 0
    for y in range(1, num_rows - 1):
        for x in range(1, num_cols - 1):
            row = tree_grid[y]
            col = [r[x] for r in tree_grid]
            h_score = utils.get_scenic_score(row, x)
            if h_score == 0:
                continue
            v_score = utils.get_scenic_score(col, y)
            if v_score == 0:
                continue
            scenic_score = h_score * v_score
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


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
