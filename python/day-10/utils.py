OP_CYCLES = {
    "noop": 1,
    "addx": 2,
}


def get_command_cycles(command):
    """Given a command string, return how many cycles the command requires
    to execute"""
    parts = command.split()
    op = parts[0]
    return OP_CYCLES.get(op)


def expand_command(command):
    """Given a command, expand the command into a list of cycles,
    with each entry showing the command being executed, and the
    amount of change to the X register after that cycle"""
    num_cycles = get_command_cycles(command)
    parts = command.split()
    if len(parts) > 1:
        op, arg = parts
    else:
        op = parts[0]
        arg = 0

    cycles = [(command, 0)] * (num_cycles - 1)
    cycles += [(command, int(arg))]

    return cycles


def expand_program(command_list):
    """Given a list of strings representing a program, expand the program
    into a list of individual cycles, with the command and the change to
    the X register in each cycle"""
    cycles = []
    for command in command_list:
        cycles += expand_command(command)

    return cycles


def format_crt_string(crt_values, cols=40):
    """Given a list of crt pixel values (True or False), create a string
    representing a 40-pixel wide screen, with "#" indicating a lit pixel
    and "." indicating an unlit pixel."""
    chars = []
    for i, value in enumerate(crt_values, start=1):
        if value:
            chars.append("#")
        else:
            chars.append(".")
        if i % cols == 0:
            chars.append("\n")
    return ''.join(chars)


