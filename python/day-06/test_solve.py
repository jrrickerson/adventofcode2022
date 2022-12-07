import solve
import utils


def test_is_set_span_empty():
    span = ""

    assert utils.is_set_span(span)


def test_is_set_span_all_one_character():
    span = "AAAA"

    assert not utils.is_set_span(span)


def test_is_set_span_all_one_duplicate():
    span = "ABCA"

    assert not utils.is_set_span(span)


def test_is_set_span_no_duplicates():
    span = "ABCD"

    assert utils.is_set_span(span)


def test_find_set_span_empty():
    sequence = ""

    start = utils.find_set_span(sequence, size=4)

    assert start is None


def test_find_set_span_no_set():
    sequence = "ABCBABBCABCAB"

    start = utils.find_set_span(sequence, size=4)

    assert start is None


def test_find_set_span_sequence_start():
    sequence = "ABCDABBCABCAB"

    start = utils.find_set_span(sequence, size=4)

    assert start == 0


def test_find_set_span_sequence_end():
    sequence = "ABCBABBCABCABX"

    start = utils.find_set_span(sequence, size=4)

    assert start == sequence.find("CABX")


def test_find_set_span_sequence_middle():
    sequence = "ABCBABCDBCABCABX"

    start = utils.find_set_span(sequence, size=4)

    assert start == sequence.find("ABCD")


def test_part_1_sample_input():
    input_data = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ]

    expected_results = [
        7,
        5,
        6,
        10,
        11,
    ]

    for data, expected in zip(input_data, expected_results):
        index = solve.part_1([data])
        assert index == expected
