import collections
import heapq
import math

GRID_CELL_OFFSET = ord("a")


def generate_grid_map(input_lines):
    """Given a list of strings, create a 2d grid based on the ordinal values
    of the characters in the strings"""
    grid = []
    if not input_lines:
        return grid
    for line in input_lines:
        grid.append([ord(char) - GRID_CELL_OFFSET for char in line])

    return grid


def find_marker_point(grid, marker="S"):
    """Find a specific character marker (i.e. start point or end point)
    in the grid and return the x, y coordinates"""
    start = (None, None)
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == ord(marker) - GRID_CELL_OFFSET:
                start = (x, y)
                break
        if cell == ord(marker) - GRID_CELL_OFFSET:
            break
    return start


def manhattan_dist(start, end):
    """Given a start point and an end point on a 2d grid, calculate
    the "Manhattan" distance - the integer distance of "blocks" to
    the target.
    https://en.wikipedia.org/wiki/Taxicab_geometry"""

    x_dist = abs(end[0] - start[0])
    y_dist = abs(end[1] - start[1])

    return x_dist + y_dist


def find_heightmap_neighbors(current, grid, max_hop=1):
    """Given a current position and the full grid of cells, find
    all valid neighbors of the current cell that can be moved to.
    Neighbors cannot be more than max_hop higher than the current
    node."""
    MAX_Y = len(grid)
    MAX_X = len(grid[0])
    neighbors = [
        (current[0] - 1, current[1]),
        (current[0] + 1, current[1]),
        (current[0], current[1] - 1),
        (current[0], current[1] + 1),
    ]

    # Remove cells that are off the grid
    valid_neighbors = [p for p in neighbors if 0 <= p[0] < MAX_X and 0 <= p[1] < MAX_Y]
    # Remove cells unreachable by height value
    valid_neighbors = [
        n
        for n in valid_neighbors
        if grid[n[1]][n[0]] <= grid[current[1]][current[0]] + max_hop
    ]
    return valid_neighbors


def construct_path(path_nodes, end_node):
    if not path_nodes:
        return []
    path = [end_node]
    node = end_node
    while node in path_nodes:
        node = path_nodes[node]
        path.append(node)
    path.reverse()
    return path


def A_star(start, end, h_func=None, neighbors=None):
    """Implements the A* pathfinding algorithm.  Given a start and end
    point, find the optimal path. Uses the h_func callable to get an
    estimated cost of the path from a point to the end point.
    Assumptions:
     - The distance to each neighbor of a cell is the Manhattan distance
     - The neighbors callable returns a list of valid neighbor cells,
       taking into account impassable paths, etc.
    """
    path_nodes = {}
    candidates = [(0, start)]
    heapq.heapify(candidates)

    # Score of the best current path from start to the key node
    g_score = collections.defaultdict(lambda: math.inf)
    # Estimated score of the path going through the key node to the end
    f_score = collections.defaultdict(lambda: math.inf)

    # Add g_score and f_score of the start point
    g_score[start] = 0
    f_score[start] = h_func(start)

    while candidates:
        # Get the candidate with the lowest fscore (top of the heap)
        _, current = heapq.heappop(candidates)

        if current == end:
            return path_nodes, current

        for neighbor in neighbors(current):
            candidate_gscore = g_score[current] + manhattan_dist(current, neighbor)

            if candidate_gscore < g_score[neighbor]:
                path_nodes[neighbor] = current
                g_score[neighbor] = candidate_gscore
                f_score[neighbor] = candidate_gscore + h_func(neighbor)
                if neighbor not in candidates:
                    heapq.heappush(candidates, (f_score[neighbor], neighbor))

    return {}, None
