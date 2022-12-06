import solve
import utils


def test_split_crates_empty():
    line = ""

    crates = utils.split_crates(line)

    assert crates == []


def test_split_crates_no_crates():
    line = "            "

    crates = utils.split_crates(line)

    assert len(crates) == 3
    assert all([c == "" for c in crates])


def test_split_crates_first_column():
    line = "[A]        "

    crates = utils.split_crates(line)

    assert len(crates) == 3
    assert crates[0] == "A"
    assert all([c == "" for c in crates[1:]])


def test_split_crates_last_column():
    line = "        [Z]"

    crates = utils.split_crates(line)

    assert len(crates) == 3
    assert crates[-1] == "Z"
    assert all([c == "" for c in crates[:-1]])


def test_split_crates_all_columsn():
    line = "[A] [X] [Z]"

    crates = utils.split_crates(line)

    assert len(crates) == 3
    assert crates == ["A", "X", "Z"]


def test_read_stack_diagram_empty():
    lines = []

    stacks = utils.read_stack_diagram(lines)

    assert stacks == []


def test_read_stack_diagram_no_crates():
    lines = [" 1   2   3   4   5   6   7   8   9 ", ""]

    stacks = utils.read_stack_diagram(lines)

    assert len(stacks) == 9
    assert all([s == [] for s in stacks])


def test_read_stack_diagram_one_level():
    lines = [
        "[A] [B] [C] [D] [E] [F] [G] [H] [I]",
        " 1   2   3   4   5   6   7   8   9 ",
        "",
    ]

    stacks = utils.read_stack_diagram(lines)

    assert len(stacks) == 9
    expected_letters = "ABCDEFGHI"
    for i in range(9):
        assert stacks[i][0] == expected_letters[i]


def test_read_stack_diagram_multi_level():
    lines = [
        "[A] [B] [C] [D] [E] [F] [G] [H] [I]",
        "[J] [K] [L] [M] [N] [O] [P] [Q] [R]",
        " 1   2   3   4   5   6   7   8   9 ",
        "",
    ]

    stacks = utils.read_stack_diagram(lines)

    assert len(stacks) == 9
    expected_letters = "JKLMNOPQR"
    for i in range(9):
        assert stacks[i][0] == expected_letters[i]
    expected_letters = "ABCDEFGHI"
    for i in range(9):
        assert stacks[i][1] == expected_letters[i]


def test_read_stack_diagram_sparse_level():
    lines = [
        "[A]     [B]         [C] [D]        ",
        " 1   2   3   4   5   6   7   8   9 ",
        "",
    ]

    stacks = utils.read_stack_diagram(lines)
    assert len(stacks) == 9
    assert stacks[0][0] == "A"
    assert stacks[2][0] == "B"
    assert stacks[5][0] == "C"
    assert stacks[6][0] == "D"


def test_read_crane_instructions_empty():
    lines = []

    instructions = utils.read_crane_instructions(lines)

    assert instructions == []


def test_read_crane_instructions_match_prefix():
    lines = [
        "",
        "1 2 3 4 5",
        "",
        "move 1 from 3 to 5",
    ]

    instructions = utils.read_crane_instructions(lines)

    assert len(instructions) == 1
    assert instructions[0] == (1, 3, 5)


def test_read_crane_instructions_invalid_line():
    lines = [
        "",
        "1 2 3 4 5",
        "",
        "move Q from 3 to 5",
    ]

    instructions = utils.read_crane_instructions(lines)

    assert len(instructions) == 1
    assert instructions[0] == (0, 0, 0)


def test_read_crane_instructions_multi_lines():
    lines = [
        "",
        "1 2 3 4 5",
        "",
        "move 1 from 3 to 5",
        "move 3 from 2 to 7",
        "move 1 from 9 to 7",
    ]

    instructions = utils.read_crane_instructions(lines)

    assert len(instructions) == 3
    assert instructions[0] == (1, 3, 5)
    assert instructions[1] == (3, 2, 7)
    assert instructions[2] == (1, 9, 7)


def test_operate_crane_no_instructions():
    instructions = []
    initial_stacks = [["A"], ["B"], ["C"]]

    stacks = utils.operate_crane(initial_stacks, instructions)

    assert stacks == initial_stacks


def test_operate_crane_single_instruction():
    instructions = [(1, 1, 3)]
    initial_stacks = [["A"], [], []]

    stacks = utils.operate_crane(initial_stacks, instructions)

    assert len(stacks) == len(initial_stacks)
    assert stacks == [[], [], ["A"]]


def test_operate_crane_fifo_ordering():
    instructions = [(3, 1, 3)]
    initial_stacks = [["A", "B", "C"], [], []]

    stacks = utils.operate_crane(initial_stacks, instructions)

    assert len(stacks) == len(initial_stacks)
    assert stacks == [[], [], ["C", "B", "A"]]


def test_operate_crane_multi_instructions():
    instructions = [
        (1, 1, 3),
        (2, 2, 1),
        (1, 3, 2),
        (2, 1, 2),
    ]
    initial_stacks = [["A", "B", "C"], ["D", "E"], ["F"]]

    stacks = utils.operate_crane(initial_stacks, instructions)

    expected_stacks = [["A", "B"], ["C", "D", "E"], ["F"]]
    assert len(stacks) == len(initial_stacks)
    assert stacks == expected_stacks


def test_part_1_sample_input():
    input_data = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    result = solve.part_1(input_data)

    assert result == "CMZ"


def test_operate_crane_multi_mode():
    instructions = [
        (1, 1, 3),
        (2, 2, 1),
        (3, 1, 3),
    ]
    initial_stacks = [["A", "B", "C"], ["D", "E"], ["F"]]

    stacks = utils.operate_crane(initial_stacks, instructions, mode="multi")

    expected_stacks = [["A"], [], ["F", "C", "B", "D", "E"]]
    assert len(stacks) == len(initial_stacks)
    assert stacks == expected_stacks


def test_part_2_sample_input():
    input_data = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    result = solve.part_2(input_data)

    assert result == "MCD"
