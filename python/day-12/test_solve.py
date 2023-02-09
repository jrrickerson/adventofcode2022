import copy

import solve
import utils


def test_generate_grid_map_empty():
    input_lines = []

    grid_map = utils.generate_grid_map(input_lines)

    assert grid_map == []


def test_generate_grid_map_single_row():
    input_lines = [
        "abaaabbbbcccdededef",
    ]

    grid_map = utils.generate_grid_map(input_lines)

    assert len(grid_map) == 1
    for x, cell in enumerate(grid_map[0]):
        assert cell == ord(input_lines[0][x]) - utils.GRID_CELL_OFFSET


def test_generate_grid_map_multiple_row():
    input_lines = [
        "abaaabbbbcccdededef",
        "aabbbaaaacccccccdef",
    ]

    grid_map = utils.generate_grid_map(input_lines)

    assert len(grid_map) == 2
    for y, line in enumerate(grid_map):
        for x, cell in enumerate(line):
            assert cell == ord(input_lines[y][x]) - utils.GRID_CELL_OFFSET


def test_normalize_heightmap_empty_map():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    original_grid = copy.deepcopy(grid)

    utils.normalize_heightmap(grid, {})

    assert grid == original_grid


def test_normalize_heightmap_replaces_positions():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccE"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aSaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]
    original_grid = copy.deepcopy(grid)

    start = (1, 1)
    end = (8, 0)
    utils.normalize_heightmap(grid, {start: "a", end: "z"})

    assert grid[start[1]][start[0]] == ord("a") - utils.GRID_CELL_OFFSET
    assert grid[end[1]][end[0]] == ord("z") - utils.GRID_CELL_OFFSET


def test_find_marker_point_does_not_exist():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    start_point = utils.find_marker_point(grid)

    assert start_point == (None, None)


def test_find_marker_point_edge():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "Sbaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    start_point = utils.find_marker_point(grid)

    assert start_point == (0, 1)


def test_find_marker_point_middle():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abaSabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    print(grid)
    start_point = utils.find_marker_point(grid)

    assert start_point == (3, 1)


def test_find_end_point_does_not_exist():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    end_point = utils.find_marker_point(grid, marker="E")

    assert end_point == (None, None)


def test_find_end_point_middle():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abaaabEcc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]

    end_point = utils.find_marker_point(grid, marker="E")

    assert end_point == (6, 1)


def test_manhattan_dist_horizontal():
    start = (0, 0)
    end = (7, 0)

    dist = utils.manhattan_dist(start, end)

    assert dist == 7


def test_manhattan_dist_vertical():
    start = (0, 0)
    end = (0, 7)

    dist = utils.manhattan_dist(start, end)

    assert dist == 7


def test_manhattan_dist_both_components():
    start = (1, 8)
    end = (5, 3)

    dist = utils.manhattan_dist(start, end)

    assert dist == 9


def test_manhattan_dist_same_point():
    start = (1, 8)
    end = (1, 8)

    dist = utils.manhattan_dist(start, end)

    assert dist == 0


def test_manhattan_dist_end_before_start():
    start = (2, 5)
    end = (0, 0)

    dist = utils.manhattan_dist(start, end)

    assert dist == 7


def test_find_heightmap_neighbors_single_cell():
    grid = [[0]]
    current = (0, 0)

    neighbors = utils.find_heightmap_neighbors(current, grid)

    assert len(neighbors) == 0


def test_find_heightmap_neighbors_edge_cell():
    grid = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    current = (0, 0)

    neighbors = utils.find_heightmap_neighbors(current, grid)

    assert len(neighbors) == 2
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors


def test_find_heightmap_neighbors_center_cell():
    grid = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    current = (1, 1)

    neighbors = utils.find_heightmap_neighbors(current, grid)

    assert len(neighbors) == 4
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors
    assert (2, 1) in neighbors
    assert (1, 2) in neighbors


def test_find_heightmap_neighbors_filter_by_height():
    grid = [[0, 1, 2], [1, 2, 3], [2, 4, 4]]
    current = (1, 1)

    neighbors = utils.find_heightmap_neighbors(current, grid)

    assert len(neighbors) == 3
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors
    assert (2, 1) in neighbors


def test_construct_path_empty():
    path_nodes = {}
    endpoint = (5, 5)

    path = utils.construct_path(path_nodes, endpoint)

    assert path == []


def test_construct_path_single_entry():
    path_nodes = {(5, 5): (4, 4)}
    endpoint = (5, 5)

    path = utils.construct_path(path_nodes, endpoint)

    assert path == [(4, 4), endpoint]


def test_construct_path_multi_entries():
    path_nodes = {
        (5, 5): (4, 4),
        (4, 4): (3, 3),
        (3, 3): (2, 2),
        (2, 2): (1, 1),
    }
    endpoint = (5, 5)

    path = utils.construct_path(path_nodes, endpoint)

    assert len(path) == 5
    assert path[0] == (1, 1)
    assert path[1] == (2, 2)
    assert path[2] == (3, 3)
    assert path[3] == (4, 4)
    assert path[4] == (5, 5)


def test_A_star_straight_line_horizontal():
    start = (0, 0)
    end = (9, 0)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)

    assert path == [(x, 0) for x in range(10)]


def test_A_star_straight_line_vertical():
    start = (0, 0)
    end = (0, 9)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)

    assert path == [(0, y) for y in range(10)]


def test_A_star_straight_line_diagonal():
    start = (0, 0)
    end = (5, 5)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)
    print("Found Path:", path)

    assert len(path) == 11


def test_A_star_handle_obstacle():
    start = (0, 0)
    end = (5, 5)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        if (0, 3) in neighbors:
            neighbors.remove((0, 3))
        if (3, 0) in neighbors:
            neighbors.remove((3, 0))
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)
    print("Found Path:", path)

    assert len(path) == 11


def test_A_star_handle_single_path():
    start = (0, 0)
    end = (5, 5)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        exclude = []
        for cell in neighbors:
            if cell[0] == 3 and cell[1] <= 4:
                exclude.append(cell)
        for cell in exclude:
            neighbors.remove(cell)
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)
    print("Found Path:", path)

    assert len(path) == 11


def test_A_star_handle_no_path():
    start = (0, 0)
    end = (5, 5)

    def hfunc(node):
        return utils.manhattan_dist(node, end)

    # Bounded grid with no solution
    def neighbors(node):
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        exclude = []
        for cell in neighbors:
            if cell[0] < 0 or cell[1] < 0:
                exclude.append(cell)
            if cell[0] == 3 or cell[1] == 3:
                exclude.append(cell)
        for cell in exclude:
            neighbors.remove(cell)
        return neighbors

    path_nodes, endpoint = utils.A_star(start, end, h_func=hfunc, neighbors=neighbors)
    print(path_nodes, endpoint)
    path = utils.construct_path(path_nodes, endpoint)

    assert path_nodes == {}
    assert endpoint is None
    assert len(path) == 0


def test_find_shortest_path_calls_A_star():
    grid = [
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaabbbccd"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "aaaaabccc"],
        [ord(c) - utils.GRID_CELL_OFFSET for c in "abababcdd"],
    ]
    start = (1, 1)
    end = (8, 0)

    path = utils.find_shortest_path(grid, start, end)

    assert len(path) == 9


def test_part_1_sample_input():
    input_data = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]

    result = solve.part_1(input_data)

    assert result == 31


def test_part_2_sample_input():
    input_data = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]

    result = solve.part_2(input_data)

    assert result == 29
