import solve
import utils


def test_convert_int_list_empty():
    input_list = []
    result = utils.convert_int_list(input_list)

    assert result == []


def test_convert_int_list_no_separators():
    input_list = ["1", "2", "3"]
    result = utils.convert_int_list(input_list)

    assert result == [1, 2, 3]


def test_convert_int_list_with_separators():
    input_list = ["1", "2", "3", "", "4", "5", "6", "", "7", "8"]
    result = utils.convert_int_list(input_list)

    assert result == [1, 2, 3, None, 4, 5, 6, None, 7, 8]


def test_partition_list_empty():
    input_list = []

    result = utils.partition_list(input_list)

    assert result == []


def test_partition_list_single_partition():
    input_list = ["1", "2", "3"]

    result = utils.partition_list(input_list)

    assert result == [["1", "2", "3"]]


def test_partition_list_single_separator():
    input_list = ["1", "2", "3", "", "4", "5"]

    result = utils.partition_list(input_list)

    assert result == [["1", "2", "3"], ["4", "5"]]


def test_partition_list_integers():
    input_list = [1, 2, 3, None, 4, 5]

    result = utils.partition_list(input_list)

    assert result == [[1, 2, 3], [4, 5]]


def test_sum_partitions_empty():
    parts = []

    result = utils.sum_partitions(parts)

    assert result == []


def test_sum_partitions_single_part():
    parts = [[1, 11, 48]]

    result = utils.sum_partitions(parts)

    assert result == [60]


def test_sum_partitions_multi_parts():
    parts = [[1, 11, 48], [4, 5, 6], [7, 10, 15]]

    result = utils.sum_partitions(parts)

    assert result == [60, 15, 32]


def test_part_1_sample_input():
    calorie_list = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]

    result = solve.part_1(calorie_list)

    assert result == 24000


def test_part_2_sample_input():
    calorie_list = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]

    result = solve.part_2(calorie_list)

    assert result == 45000

