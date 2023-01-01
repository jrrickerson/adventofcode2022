

def parse_command(lines):
    """Parse a bash-like command from a list of strings.
    Commands are prefixed with a "$ " and may have one or more args
    Lines following the command without the "$ " prefix are considered
    ouput for the command.
    Examples:
        $ ls
        abc.txt
        123.dat
        $ cd hello
        $ cd ..
    """
    if not lines:
        return None, None
    if not lines[0].startswith("$ "):
        return None, None

    line = lines.pop(0)
    cmdline = tuple(line[2:].strip().split())
    output_lines = []
    while lines and not lines[0].startswith("$ "):
        output_lines.append(lines.pop(0))

    return cmdline, output_lines


def parse_listing(lines):
    """Parse a directory listing output by the "ls" command.
    Files are output as size, name tuples, whereas directories
    are output as "dir" followed by the name.
    Returns a dictionary of the entries keyed by name, with integer
    sizes for the files and empty dictionaries for the subdirectories."""
    entries = {}
    # Add subdirectories
    dirs = [line.split()[1] for line in lines if line.startswith("dir")]
    files = [line.split() for line in lines if not line.startswith("dir")]
    entries.update({dirname: {"__name__": dirname} for dirname in dirs})
    entries.update({filename: int(size) for size, filename in files})

    return entries


def attach_directory(name, entries, parent):
    """Attach a new directory to the directory tree by creating or
    updating a dictionary of entries, and including a special ".."
    entry pointing back to the parent directory."""
    if name == "/":
        directory = parent
    else:
        directory = parent.setdefault(name, {})

    entries[".."] = parent
    directory.update(entries)
    directory["__name__"] = name

    return directory


def handle_change_directory(dirname, cwd, root, path_stack, output):
    """Given a target directory name, a root directory, and
    a current working directory, change the current working
    directory, if possible, to the target directory"""
    if dirname == "/":
        cwd = root
        path_stack.clear()
        return cwd
    if dirname not in cwd:
        print(f"ERROR: Invalid subdirectory {dirname}")
        return cwd

    cwd = cwd.get(dirname, cwd)
    if dirname == "..":
        path_stack.pop()
    else:
        path_stack.append(cwd)

    return cwd


def handle_list_directory(cwd, root, path_stack, output):
    dir_entries = parse_listing(output)
    parent = cwd.get("..", path_stack[-2] if len(path_stack) > 1 else root)
    name = cwd.get("__name__", None)

    attach_directory(name, dir_entries, parent)

    return cwd


def create_directory_tree(input_lines):
    CLI_COMMAND_MAP = {
        "cd": handle_change_directory,
        "ls": handle_list_directory,
    }
    lines = input_lines.copy()

    root_dir = {"__name__": "/"}
    cwd = root_dir
    path_stack = []
    while lines:
        cmdline, cmdout = parse_command(lines)
        cmd, *args = cmdline
        command_func = CLI_COMMAND_MAP.get(cmd)
        cwd = command_func(*args, cwd=cwd, root=root_dir,
                           path_stack=path_stack, output=cmdout)

    return root_dir



def find_directory_sizes(directory, path, sizes=None, recursive=True):
    """Given a directory, find the size of all files within it.
    Recursive flag indicates that all sizes of subdirectories are included
    in the returned sizes"""

    sizes = sizes if sizes is not None else {}

    subdirs = [name for name, subdir in directory.items()
              if isinstance(subdir, dict) and name != ".."]
    dirsize = (
        sum([size for name, size in directory.items() if isinstance(size, int)]) +
        sum([find_directory_sizes(directory[name], path + f"{name}/", sizes=sizes)
            for name in subdirs]))

    sizes[path] = dirsize
    return dirsize
