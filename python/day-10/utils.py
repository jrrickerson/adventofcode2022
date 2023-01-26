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
