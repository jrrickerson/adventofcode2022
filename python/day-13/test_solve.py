import solve
import utils


def test_parse_packet_empty():
    packet_line = ""

    packet = utils.parse_packet(packet_line)

    assert packet is None


def test_parse_packet_empty_list():
    packet_line = "[]"

    packet = utils.parse_packet(packet_line)

    assert packet == []


def test_parse_packet_integer_list():
    packet_line = "[1, 2, 3]"

    packet = utils.parse_packet(packet_line)

    assert packet == [1, 2, 3]


def test_parse_packet_nested_list():
    packet_line = "[[1], [2, 3]]"

    packet = utils.parse_packet(packet_line)

    assert packet == [[1], [2, 3]]


def test_compare_integers_ordered():
    left = 1
    right = 2

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_integers_unordered():
    left = 2
    right = 1

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_integers_equal():
    left = 1
    right = 1

    order = utils.compare(left, right)

    assert 0 == order


def test_compare_single_element_lists_ordered():
    left = [1]
    right = [2]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_single_element_lists_unordered():
    left = [2]
    right = [1]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_single_element_lists_equal():
    left = [1]
    right = [1]

    order = utils.compare(left, right)

    assert 0 == order


def test_compare_multi_element_lists_ordered():
    left = [1, 2, 3]
    right = [2, 3, 4]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_multi_element_lists_unordered():
    left = [2, 3, 4]
    right = [1, 2, 3]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_multi_element_lists_equal():
    left = [1, 2, 3]
    right = [1, 2, 3]

    order = utils.compare(left, right)

    assert 0 == order


def test_compare_multi_element_lists_same_prefix():
    left = [1, 2, 3]
    right = [1, 2, 4]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_nested_list():
    left = [[1], [2, 3]]
    right = [[1], [2, 4]]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_nested_list_wrong_order():
    left = [[1], [2, 4]]
    right = [[1], [2, 3]]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_shorter_list_left():
    left = [1, 2]
    right = [1, 2, 4]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_shorter_list_right():
    left = [1, 2, 3]
    right = [1, 2]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_mixed_type_int_left():
    left = [1, 2, 3]
    right = [[1], 2, 4]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_mixed_type_int_left_unordered():
    left = [1, 2, 3]
    right = [[0], 2, 4]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_mixed_type_int_right_ordered():
    left = [[1], 2, 3]
    right = [2, 2, 4]

    order = utils.compare(left, right)

    assert -1 == order


def test_compare_mixed_type_int_right_unordered():
    left = [[1], 2, 3]
    right = [0, 2, 4]

    order = utils.compare(left, right)

    assert 1 == order


def test_compare_sample_data_1():
    left = "[1,1,3,1,1]"
    right = "[1,1,5,1,1]"

    order = utils.compare(utils.parse_packet(left), utils.parse_packet(right))

    assert -1 == order


def test_compare_sample_data_2():
    left = "[[1],[2,3,4]]"
    right = "[[1],4]"

    order = utils.compare(utils.parse_packet(left), utils.parse_packet(right))

    assert -1 == order


def test_compare_sample_data_3():
    left = "[9]"
    right = "[[8,7,6]]"

    order = utils.compare(utils.parse_packet(left), utils.parse_packet(right))

    assert 1 == order


def test_compare_sample_data_4():
    left = "[[4,4],4,4]"
    right = "[[4,4],4,4,4]"

    order = utils.compare(utils.parse_packet(left), utils.parse_packet(right))

    assert -1 == order


def test_part_1_sample_data():
    input_data = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "[9]",
        "[[8,7,6]]",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "[7,7,7,7]",
        "[7,7,7]",
        "[]",
        "[3]",
        "[[[]]]",
        "[[]]",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    result = solve.part_1(input_data)

    assert result == 13


def test_part_2_sample_data():
    input_data = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "[9]",
        "[[8,7,6]]",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "[7,7,7,7]",
        "[7,7,7]",
        "[]",
        "[3]",
        "[[[]]]",
        "[[]]",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    result = solve.part_2(input_data)

    assert result == 140
