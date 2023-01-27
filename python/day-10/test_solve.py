import solve
import utils


LARGE_SAMPLE_INPUT = [
    "addx 15",
    "addx -11",
    "addx 6",
    "addx -3",
    "addx 5",
    "addx -1",
    "addx -8",
    "addx 13",
    "addx 4",
    "noop",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx -35",
    "addx 1",
    "addx 24",
    "addx -19",
    "addx 1",
    "addx 16",
    "addx -11",
    "noop",
    "noop",
    "addx 21",
    "addx -15",
    "noop",
    "noop",
    "addx -3",
    "addx 9",
    "addx 1",
    "addx -3",
    "addx 8",
    "addx 1",
    "addx 5",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx -36",
    "noop",
    "addx 1",
    "addx 7",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "addx 6",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx 7",
    "addx 1",
    "noop",
    "addx -13",
    "addx 13",
    "addx 7",
    "noop",
    "addx 1",
    "addx -33",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "noop",
    "noop",
    "noop",
    "addx 8",
    "noop",
    "addx -1",
    "addx 2",
    "addx 1",
    "noop",
    "addx 17",
    "addx -9",
    "addx 1",
    "addx 1",
    "addx -3",
    "addx 11",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx -13",
    "addx -19",
    "addx 1",
    "addx 3",
    "addx 26",
    "addx -30",
    "addx 12",
    "addx -1",
    "addx 3",
    "addx 1",
    "noop",
    "noop",
    "noop",
    "addx -9",
    "addx 18",
    "addx 1",
    "addx 2",
    "noop",
    "noop",
    "addx 9",
    "noop",
    "noop",
    "noop",
    "addx -1",
    "addx 2",
    "addx -37",
    "addx 1",
    "addx 3",
    "noop",
    "addx 15",
    "addx -21",
    "addx 22",
    "addx -6",
    "addx 1",
    "noop",
    "addx 2",
    "addx 1",
    "noop",
    "addx -10",
    "noop",
    "noop",
    "addx 20",
    "addx 1",
    "addx 2",
    "addx 2",
    "addx -6",
    "addx -11",
    "noop",
    "noop",
    "noop",
]

def test_get_command_cycles_noop():
    command = "noop"

    cycles = utils.get_command_cycles(command)

    assert cycles == 1


def test_get_command_cycles_addx():
    command = "addx 3"

    cycles = utils.get_command_cycles(command)

    assert cycles == 2


def test_expand_command_noop():
    command = "noop"

    cycles = utils.expand_command(command)

    assert cycles[0] == ("noop", 0)


def test_expand_command_addx_positive():
    command = "addx 3"

    cycles = utils.expand_command(command)

    assert cycles[-1][1] == 3
    for cycle in cycles[:-1]:
        assert cycle[1] == 0


def test_expand_command_addx_negative():
    command = "addx -2"

    cycles = utils.expand_command(command)

    assert cycles[-1][1] == -2
    for cycle in cycles[:-1]:
        assert cycle[1] == 0


def test_expand_program_empty():
    commands = []

    cycles = utils.expand_program(commands)

    assert len(cycles) == 0


def test_expand_program_single_cycle():
    commands = [
        "noop",
    ]

    cycles = utils.expand_program(commands)

    assert len(cycles) == 1


def test_expand_program_multi_cycle():
    commands = [
        "addx 5",
    ]

    cycles = utils.expand_program(commands)

    assert len(cycles) == 2


def test_expand_program_mixed_commands():
    commands = [
        "noop",
        "addx 3",
        "addx -5",
    ]

    cycles = utils.expand_program(commands)

    assert len(cycles) == 5
    assert cycles[0] == ("noop", 0)
    assert cycles[2] == ("addx 3", 3)
    assert cycles[4] == ("addx -5", -5)


def test_part_1_sample_input():
    input_data = LARGE_SAMPLE_INPUT

    result = solve.part_1(input_data)

    assert result == 13140


def test_format_crt_string_empty():
    crt = []

    screen = utils.format_crt_string(crt)

    assert screen == ""


def test_format_crt_string_all_off():
    crt = [False, False, False, False, False, False]

    screen = utils.format_crt_string(crt)

    assert "#" not in screen


def test_format_crt_string_all_on():
    crt = [True, True, True, True, True]

    screen = utils.format_crt_string(crt)

    assert "." not in screen


def test_format_crt_string_mixed_values():
    crt = [True, True, False, True, True, False]

    screen = utils.format_crt_string(crt)

    assert "##.##." == screen


def test_format_crt_string_line_breaks():
    crt = [True] * 95

    screen = utils.format_crt_string(crt)

    print(screen)
    assert len(screen) == len(crt) + (len(crt) // 40)
    assert screen[40] == "\n"
    assert screen[81] == "\n"


def test_part_2_sample_input():
    input_data = LARGE_SAMPLE_INPUT

    expected_result = "\n".join([
        "\n##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....\n",
    ])

    result = solve.part_2(input_data)

    assert result == expected_result
