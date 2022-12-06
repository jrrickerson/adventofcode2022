def split_crates(crate_line):
    """Given a line of text, find all 3 character representations of crates
    i.e. "[A]" based on their positions in the line.  A crate position may
    contain only spaces to indicate no crate exists at that position"""
    crates = [crate_line[idx : idx + 4].strip() for idx in range(0, len(crate_line), 4)]
    # Extract just the letter for each crate if there is one
    return [crate[1] if crate else "" for crate in crates]


def read_stack_diagram(lines):
    """Given a list of lines including a diagram of stacks of crates at the top,
    generate a list of lists representing the stacks in the diagram."""
    if not lines:
        return []

    # Slice to the first blank line
    diagram_lines = lines[: lines.index("")]

    # Flip the diagram upside down to build stack lists
    diagram_lines.reverse()
    # Read the stack header and determine how many stacks are needed
    stack_header = [int(label) for label in diagram_lines[0].split()]
    stacks = [list() for i in range(max(stack_header))]

    # Parse the list of crates line by line and put them into the appropriate
    # stack, matched by index order
    for crate_line in diagram_lines[1:]:
        crates = split_crates(crate_line)
        for stack, crate in zip(stacks, crates):
            if crate:
                stack.append(crate)
    return stacks


def read_crane_instructions(lines):
    """Given lines from a file, find all lines that match the format
    "move X from Y to Z" and parse them into a list of 3-element tuples
    containing the quantity of crates, source stack, and destination stack"""

    instruction_lines = [line for line in lines if line.startswith("move")]

    instructions = []
    for text in instruction_lines:
        tokens = text.split()
        prev = ""
        qty, src, dest = 0, 0, 0
        for token in tokens:
            try:
                if prev == "move":
                    qty = int(token)
                elif prev == "from":
                    src = int(token)
                elif prev == "to":
                    dest = int(token)
            except ValueError:
                print(f"Skipping invalid token {token} after prefix {prev}")
                qty, src, dest = 0, 0, 0  # NOOP instruction
                break
            prev = token
        instructions.append((qty, src, dest))

    return instructions


def operate_crane(stacks, instructions):
    """Given a starting state of stacks of crates, and a set of instructions
    to use the crane to manipulate those stacks, perform the crane operations
    and return the resulting state of the stacks."""

    for line_num, instruction in enumerate(instructions):
        qty, source, destination = instruction
        # Correct for zero-based list indices
        src_idx = source - 1
        dest_idx = destination - 1
        for i in range(qty):
            try:
                crate = stacks[src_idx].pop()
                stacks[dest_idx].append(crate)
            except IndexError:
                print("Invalid crane instruction!")
                print("Current Stack state: ", stacks)

    return stacks
