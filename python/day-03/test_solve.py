import string

import utils
import solve


def test_split_into_empty():
    chars = ""

    parts = utils.split_into(chars, parts=2)

    assert parts[0] == ""
    assert parts[1] == ""


def test_split_into_no_remainder():
    chars = "ABCDefgh"

    parts = utils.split_into(chars, parts=2)

    assert parts[0] == "ABCD"
    assert parts[1] == "efgh"


def test_split_into_with_remainder():
    chars = "ABCDefghi"

    parts = utils.split_into(chars, parts=2)

    assert parts[0] == "ABCD"
    assert parts[1] == "efghi"


def test_split_into_non_default_count():
    chars = string.ascii_lowercase
    expected_parts = 8

    parts = utils.split_into(chars, parts=expected_parts)

    assert len(parts) == expected_parts
    assert all([len(part) >= len(chars) // expected_parts for part in parts])


def test_intersect_letters_empty():
    parts = ["", ""]

    common = utils.intersect_letters(parts)

    assert common == []


def test_intersect_letters_single_letter():
    parts = ["ABCd", "dEFG"]

    common = utils.intersect_letters(parts)

    assert common == ["d"]


def test_intersect_letters_multi_letter():
    parts = ["ABCD", "BCDE"]

    common = utils.intersect_letters(parts)

    assert "B" in common
    assert "C" in common
    assert "D" in common


def test_intersect_letters_multi_parts():
    parts = ["ABC", "BDE", "LBBL", "ZQPB"]

    common = utils.intersect_letters(parts)

    assert common == ["B"]


def test_map_priorities_empty():
    letters = ""

    priorities = utils.map_priorities(letters)

    assert priorities == []


def test_map_priorities_single_letter():
    letters = "A"

    priorities = utils.map_priorities(letters)

    assert priorities == [27]


def test_map_priorities_multi_letters():
    letters = "aABc"

    priorities = utils.map_priorities(letters)

    assert priorities == [1, 27, 28, 3]


def test_part_1_sample_input():
    input_data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    total_priority = solve.part_1(input_data)

    assert total_priority == 157


def test_part_2_sample_input():
    input_data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    total_priority = solve.part_2(input_data)

    assert total_priority == 70
