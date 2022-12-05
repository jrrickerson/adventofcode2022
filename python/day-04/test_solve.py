import solve
import utils


def test_split_ranges_empty():
    line = ""

    range_list = utils.split_ranges(line)

    assert len(range_list) == 1


def test_split_ranges_pair():
    line = "1-3,5-9"

    range_list = utils.split_ranges(line)

    assert len(range_list) == 2


def test_generate_range_set_empty():
    range_str = ""

    range_set = utils.generate_range_set(range_str)

    assert len(range_set) == 0
    assert type(range_set) == set


def test_generate_range_set_returns_set():
    range_str = ""

    range_set = utils.generate_range_set(range_str)

    assert type(range_set) == set


def test_generate_range_set_invalid_format():
    range_str = "invalid"

    range_set = utils.generate_range_set(range_str)

    assert len(range_set) == 0


def test_generate_range_set_single_value():
    range_str = "6-6"

    range_set = utils.generate_range_set(range_str)

    assert len(range_set) == 1
    assert 6 in range_set


def test_generate_range_set_closed_range():
    range_str = "6-7"

    range_set = utils.generate_range_set(range_str)

    assert len(range_set) == 2
    assert 6 in range_set
    assert 7 in range_set


def test_generate_range_set_double_digit_range():
    range_str = "25-47"

    range_set = utils.generate_range_set(range_str)

    assert len(range_set) == (47 + 1 - 25)
    assert 25 in range_set
    assert 47 in range_set


def test_part_1_sample_data():
    input_data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    subset_count = solve.part_1(input_data)

    assert subset_count == 2


def test_part_2_sample_data():
    input_data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    intersects = solve.part_2(input_data)

    assert intersects == 4
