import pytest

import solve
import utils


def test_parse_monkey_id_value():
    line = "Monkey 7:"

    monkey_id = utils.parse_monkey_id(line)

    assert monkey_id == 7


def test_parse_monkey_id_raise_on_invalid_line():
    line = "Hippo 7:"

    with pytest.raises(ValueError):
        monkey_id = utils.parse_monkey_id(line)


def test_parse_items_empty():
    line = "Starting items: "

    items = utils.parse_items(line)

    assert len(items) == 0


def test_parse_items_single_value():
    line = "Starting items: 12"

    items = utils.parse_items(line)

    assert len(items) == 1
    assert 12 in items


def test_parse_items_multiple_values():
    line = "Starting items: 5, 7, 14"

    items = utils.parse_items(line)

    assert len(items) == 3
    assert items == [5, 7, 14]


def test_parse_items_raise_on_invalid_line():
    line = "Monkey 0:"

    with pytest.raises(ValueError):
        items = utils.parse_items(line)


def test_parse_operation_addition():
    line = "Operation: new = old + 17"

    op = utils.parse_operation(line)

    assert callable(op)
    assert op(1) == 1 + 17
    assert op(17) == 17 + 17


def test_parse_operation_multiplication():
    line = "Operation: new = old * 5"

    op = utils.parse_operation(line)

    assert callable(op)
    assert op(1) == 1 * 5
    assert op(12) == 12 * 5


def test_parse_operation_square():
    line = "Operation: new = old * old"

    op = utils.parse_operation(line)

    assert callable(op)
    assert op(1) == 1 * 1
    assert op(12) == 12 * 12


def test_parse_operation_raise_on_invalid_line():
    line = "Starting items: 1, 2, 3"

    with pytest.raises(ValueError):
        items = utils.parse_operation(line)


def test_parse_operation_raise_on_unsupported_operator():
    line = "Operation: new = old / 3"

    with pytest.raises(KeyError):
        items = utils.parse_operation(line)


def test_parse_test_return_target_on_pass():
    lines = [
        "Test: divisible by 5",
        "  If true: throw to monkey 1",
        "  If false: throw to monkey 7",
    ]

    test_func, divisor = utils.parse_test(lines)

    assert callable(test_func)
    assert divisor == 5
    assert test_func(5) == 1
    assert test_func(10) == 1
    assert test_func(25) == 1


def test_parse_test_return_target_on_fail():
    lines = [
        "Test: divisible by 5",
        "  If true: throw to monkey 1",
        "  If false: throw to monkey 7",
    ]

    test_func, divisor = utils.parse_test(lines)

    assert callable(test_func)
    assert divisor == 5
    assert test_func(2) == 7
    assert test_func(3) == 7
    assert test_func(29) == 7


def test_parse_test_raise_on_invalid_lines():
    lines = [
        "Test: divisible by 5",
        "  If true: throw to monkey 1",
    ]

    with pytest.raises(ValueError):
        test_func, divisor = utils.parse_test(lines)


def test_parse_test_raise_on_invalid_test_definition():
    lines = [
        "Monkey: 0",
        "  If true: throw to monkey 1",
        "  If false: throw to monkey 7",
    ]

    with pytest.raises(ValueError):
        test_func, divisor = utils.parse_test(lines)


def test_parse_test_raise_on_invalid_true_condition():
    lines = [
        "Test: divisible by 5",
        "  If false: throw to monkey 7",
        "  If true: throw to monkey 1",
    ]

    with pytest.raises(ValueError):
        test_func, divisor = utils.parse_test(lines)


def test_parse_test_raise_on_invalid_false_condition():
    lines = [
        "Test: divisible by 5",
        "  If true: throw to monkey 1",
        "  If not true: throw to monkey 7",
    ]

    with pytest.raises(ValueError):
        test_func, divisor = utils.parse_test(lines)


def test_parse_monkey_returns_monkey_type():
    lines = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
    ]

    monkey = utils.parse_monkey(lines)

    assert isinstance(monkey, utils.Monkey)


def test_parse_monkey_has_correct_attributes():
    lines = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
    ]

    monkey = utils.parse_monkey(lines)

    assert monkey.id == 0
    assert monkey.items == [79, 98]
    assert monkey.inspect(12) == 12 * 19
    assert monkey.test(23) == 2
    assert monkey.test(17) == 3


def test_parse_monkey_raises_on_invalid_lines():
    lines = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
    ]

    with pytest.raises(ValueError):
        monkey = utils.parse_monkey(lines)


def test_take_turn_no_items():
    monkeys = [
        utils.Monkey(0, [], lambda w: w + 1, lambda w: w % 2, 2),
        utils.Monkey(1, [1, 2, 3], lambda w: w + 7, lambda w: w % 8, 8),
    ]

    inspect_count = utils.take_turn(monkeys[0], monkeys)

    assert inspect_count == 0


def test_take_turn_throws_all_items():
    monkeys = [
        utils.Monkey(0, [], lambda w: w + 1, lambda w: w % 2, 2),
        utils.Monkey(1, [1, 2, 3], lambda w: w + 7, lambda w: 0, 1),
    ]

    inspect_count = utils.take_turn(monkeys[1], monkeys)

    assert inspect_count == 3
    assert len(monkeys[0].items) == 3
    assert monkeys[1].items == []


def test_take_turn_worry_modified_correctly():
    monkeys = [
        utils.Monkey(0, [], lambda w: w + 1, lambda w: w % 2, 2),
        utils.Monkey(1, [1, 2, 3], lambda w: w + 7, lambda w: 0, 1),
    ]

    expected_values = [(x + 7) // 3 for x in monkeys[1].items]
    inspect_count = utils.take_turn(monkeys[1], monkeys)

    assert inspect_count == 3
    assert monkeys[0].items == expected_values


def test_take_turn_throw_to_correct_target():
    monkeys = [
        utils.Monkey(0, [], lambda w: w + 1, lambda w: w % 2, 2),
        utils.Monkey(1, [], lambda w: w + 7, lambda w: w % 2, 2),
        utils.Monkey(2, [7, 8, 12, 46], lambda w: w + 7, lambda w: w % 2, 2),
    ]

    expected_values = [(x + 7) // 3 for x in monkeys[2].items]
    inspect_count = utils.take_turn(monkeys[2], monkeys)

    assert inspect_count == 4
    for value in expected_values:
        i = value % 2
        assert value in monkeys[i].items


def test_part_1_sample_input():
    input_data = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    result = solve.part_1(input_data)

    assert result == 10605


# @pytest.mark.skip(reason="Currently runs too long")
def test_part_2_sample_input():
    input_data = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    result = solve.part_2(input_data)

    assert result == 2713310158
