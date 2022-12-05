def split_ranges(line, delimiter=","):
    """Given a string, split it by the comma character"""
    return line.split(",")


def generate_range_set(range_string, delimiter="-"):
    """Given a string representing a range in the format of 'start-end',
    create a set representing all the values within the range (closed)"""
    if not range_string:
        return set()

    boundaries = range_string.split(delimiter)
    if not len(boundaries) == 2:
        return set()

    start, end = boundaries
    range_set = set(range(int(start), int(end) + 1))
    return range_set
