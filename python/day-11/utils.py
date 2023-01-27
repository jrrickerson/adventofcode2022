import operator

from collections import namedtuple


OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}

Monkey = namedtuple(
    "Monkey", ["id", "items", "inspect", "test"])


def parse_monkey_id(line):
    if not line.startswith("Monkey"):
        raise ValueError
    return int(line.strip(":").replace("Monkey ", ""))


def parse_items(line):
    """Parse a string indicating a monkey's starting items
    into a list of integers.
    Example: 
        "Starting items: 1, 2, 3"
    Result: 
        [1, 2, 3]"""
    line = line.strip()
    if not line.startswith("Starting items:"):
        raise ValueError("Invalid item line")

    prefix, items = line.split(":")
    values = items.strip().split(", ")
    items = [int(v) for v in values if v]

    return items


def parse_operation(line):
    """Parse a string indicating an expression to modify a worry
    value after a monkey inspects an item. Returns a function of
    the form F(w) -> w where w is an integer value
    Example:
        "Operation: new = old + 8"
    Result:
        lambda old: old + 8"""
    line = line.strip()
    if not line.startswith("Operation:"):
        raise ValueError("Invalid operation line")

    _, op_string = line.split(":")

    new, equal, old, symbol, param = op_string.strip().split()
    oper = OPERATORS[symbol]
    if param == "old":
        def op_func(old):
            return oper(old, old)
    else:
        const = int(param)
        def op_func(old):
            return oper(old, const)

    return op_func


def parse_test(lines):
    """Parse a list of strings indicating the test a monkey will perform
    on the worry level of an item and which monkey he will throw to based
    on the test. Returns a function of the form F(w) -> m where w is the
    integer worry value and m is the monkey id to throw to.
    Example:
        Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
    Result:
        lambda w: 2 if w % 23 == 0 else 3"""
    if len(lines) != 3:
        raise ValueError("Expected 3 lines of input")

    test_definition = lines[0].strip()
    true_condition = lines[1].strip()
    false_condition = lines[2].strip()
    if not test_definition.startswith("Test:"):
        raise ValueError("Invalid test definition")
    if not true_condition.startswith("If true:"):
        raise ValueError("Invalid true condition")
    if not false_condition.startswith("If false:"):
        raise ValueError("Invalid false condition")

    _, test_expression = test_definition.split(": ")
    value = test_expression.lower().replace("divisible by", "")
    divisor = int(value.strip())

    _, target_expression = true_condition.split(": ")
    value = target_expression.lower().replace("throw to monkey", "")
    pass_target = int(value.strip())

    _, target_expression = false_condition.split(": ")
    value = target_expression.lower().replace("throw to monkey", "")
    fail_target = int(value.strip())

    def test_function(worry):
        if worry % divisor == 0:
            return pass_target
        else:
            return fail_target

    return test_function


def parse_monkey(lines):
    if not len(lines) == 6:
        raise ValueError("Expected 6 lines of input")

    monkey_id = parse_monkey_id(lines.pop(0))
    items = parse_items(lines.pop(0))
    operation = parse_operation(lines.pop(0))
    test = parse_test(lines)

    return Monkey(
        id=monkey_id, items=items, inspect=operation, test=test)


def take_turn(current_monkey, monkeys):
    if not current_monkey.items:
        #print(f"Monkey {current_monkey.id} - no items")
        return 0

    inspect_count = len(current_monkey.items)
    #print(f"Monkey {current_monkey.id} - {current_monkey.items}")
    while current_monkey.items:
        worry = current_monkey.items.pop(0)
        worry = current_monkey.inspect(worry)
        #print(f"   after inspect: {worry}")
        # Global reduce worry
        worry = worry // 3
        #print(f"   after bored: {worry}")
        target = current_monkey.test(worry)
        #print(f"   throw to: {target}")
        monkeys[target].items.append(worry)

    return inspect_count
