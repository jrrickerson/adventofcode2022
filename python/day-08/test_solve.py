import solve
import utils


def test_generate_grid_empty():
    input_lines = []

    grid = utils.generate_grid(input_lines)

    assert grid == []


def test_generate_grid_single_row():
    input_lines = [
        "1015981014",
    ]

    grid = utils.generate_grid(input_lines)

    assert grid == [[1, 0, 1, 5, 9, 8, 1, 0, 1, 4]]


def test_generate_grid_multi_row():
    input_lines = [
        "9810",
        "1015",
        "7629",
    ]

    grid = utils.generate_grid(input_lines)

    assert grid == [
        [9, 8, 1, 0],
        [1, 0, 1, 5],
        [7, 6, 2, 9]
    ]


def test_reduce_heights_by_zero():
    heights = [0, 2, 3, 2, 1]

    new_heights = utils.reduce_heights_by(heights, 0)

    assert new_heights == heights


def test_reduce_heights_by_specific_position():
    heights = [0, 2, 3, 2, 1]

    new_heights = utils.reduce_heights_by(heights, heights[-1])

    assert new_heights == [-1, 1, 2, 1, 0]


def test_first_visible_zero_items():
    heights = [-1, -2, -1, -3, -1, -1]

    visible_pos = utils.first_visible(heights)

    assert visible_pos is None


def test_first_visible_single_item():
    heights = [-1, -2, -1, 2, -1, -1]

    visible_pos = utils.first_visible(heights)

    assert visible_pos == 3


def test_first_visible_forward_search():
    heights = [-1, -1, 0, 2, 1, -1]

    visible_pos = utils.first_visible(heights)

    assert visible_pos == 2


def test_first_visible_reverse_search():
    heights = [-1, -1, 0, 2, 1, -1]

    visible_pos = utils.first_visible(heights, reverse=True)

    assert visible_pos == 4


def test_vectors_from_index_set_by_row():
    index_set = {1, 7, 3, 2}

    vectors = utils.vectors_from_index_set(index_set, row=1)

    assert type(vectors) is set
    assert len(vectors) == 4
    assert all([v[0] == 1 for v in vectors])


def test_vectors_from_index_set_by_col():
    index_set = {1, 7, 3, 2}

    vectors = utils.vectors_from_index_set(index_set, col=1)

    assert type(vectors) is set
    assert len(vectors) == 4
    assert all([v[1] == 1 for v in vectors])


def test_vectors_from_index_set_empty():
    index_set = set()

    vectors = utils.vectors_from_index_set(index_set, row=1)

    assert type(vectors) is set
    assert len(vectors) == 0


def test_vectors_from_index_set_no_row_no_col():
    index_set = {1, 3, 7, 9}

    vectors = utils.vectors_from_index_set(index_set)

    assert type(vectors) is set
    assert len(vectors) == 0


def test_find_visible_higher_edges():
    heights = [3, 1, 1, 1, 2]

    visible = utils.find_visible(heights)

    assert type(visible) is set
    assert len(visible) == 2
    assert 0 in visible
    assert 4 in visible


def test_find_visible_flat():
    heights = [1, 1, 1, 1, 1]

    visible = utils.find_visible(heights)

    assert type(visible) is set
    assert len(visible) == 2
    assert 0 in visible
    assert 4 in visible


def test_find_visible_single_inner():
    heights = [3, 1, 5, 1, 2]

    visible = utils.find_visible(heights)

    assert type(visible) is set
    assert len(visible) == 3
    assert 0 in visible
    assert 4 in visible
    assert 2 in visible


def test_find_visible_from_start():
    heights = [3, 4, 5, 0, 9]

    visible = utils.find_visible(heights)

    assert type(visible) is set
    assert len(visible) == 4
    assert 0 in visible
    assert 1 in visible
    assert 2 in visible
    assert 4 in visible


def test_find_visible_from_end():
    heights = [9, 4, 5, 3, 2]

    visible = utils.find_visible(heights)

    assert type(visible) is set
    assert len(visible) == 4
    assert 0 in visible
    assert 2 in visible
    assert 3 in visible
    assert 4 in visible


def test_part_1_sample_input():
    input_data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    result = solve.part_1(input_data)

    assert result == 21


def test_find_scenic_score_left_edge():
    heights = [1, 2, 1, 1, 1]
    index = 0

    score = utils.get_scenic_score(heights, index)

    assert score == 1


def test_find_scenic_score_right_edge():
    heights = [1, 2, 1, 2, 1]
    index = 4

    score = utils.get_scenic_score(heights, index)

    assert score == 1


def test_find_scenic_score_blocking_trees():
    heights = [5, 2, 3, 4, 1]
    index = 2

    score = utils.get_scenic_score(heights, index)

    assert score == 2


def test_find_scenic_score_no_blocking_trees():
    heights = [1, 2, 5, 4, 3]
    index = 2

    score = utils.get_scenic_score(heights, index)

    assert score == 4


def test_part_2_sample_input():
    input_data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    result = solve.part_2(input_data)

    assert result == 8
