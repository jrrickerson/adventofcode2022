


def generate_grid(input_lines):
    """Given a list of strings, generate a 2D grid of integers"""
    grid = [[int(cell) for cell in row] for row in input_lines]
    return grid


def reduce_heights_by(heights, value):
    """Given a series of integer values representing heights,
    reduce all the height values by the provided value"""
    return [h - value for h in heights]


def first_visible(heights, reverse=False):
    """Given a list of integer heights, find the position of the
    first visible height in the search direction (forward or reverse).
    A 'visible' height is defined as 0 or above."""
    if reverse:
        search_range = range(len(heights) - 1, -1, -1)
    else:
        search_range = range(0, len(heights))
    for pos in search_range:
        if heights[pos] >= 0:
            return pos
    return None


def vectors_from_index_set(index_set, row=None, col=None):
    """Given a set of integers, create a set of 2D vectors
    representing points along that row or col specified."""
    if row is not None:
        vectors = {(row, i) for i in index_set}
    elif col is not None:
        vectors = {(i, col) for i in index_set}
    else:
        vectors = set()

    return vectors
    

def find_visible(heights):
    """Given a sequence of heights, find all of the "visible" heights
    from the start and end of the sequence, with "visible" defined by
    having a height greater than any value before it in search order"""
    visible = set()
    from_start = 0
    start_heights = heights
    # Check from the left / top
    while from_start is not None:
        visible.add(from_start)
        start_heights = reduce_heights_by(
            start_heights, start_heights[from_start] + 1)
        from_start = first_visible(start_heights)

    # Check from the right / bottom
    from_end = len(heights) - 1
    end_heights = heights
    while from_end is not None:
        visible.add(from_end)
        end_heights = reduce_heights_by(
            end_heights, end_heights[from_end] + 1)
        from_end = first_visible(end_heights, reverse=True)

    return visible


def get_scenic_score(heights, index):
    """Given a sequence of heights and the index of a tree, calculate
    the scenic score for the tree."""
    adjusted_heights = reduce_heights_by(heights, heights[index])
    if index == 0:
        left = 1
    else:
        # Search backward from the tree to get the view distance
        start = first_visible(adjusted_heights[:index], reverse=True) or 0
        left = index - start
    if index == len(heights) - 1:
        right = 1
    else:
        # Search forward from the tree to get the view distance
        visible = first_visible(adjusted_heights[index+1:])
        right = (len(adjusted_heights) - 1 - index if visible is None else
                visible + 1)
    return left * right
