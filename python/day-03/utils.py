import string

PRIORITIES = dict(zip(string.ascii_letters, range(1, 53)))


def split_into(chars, parts=2):
    """Given an arbitrary string and a number of parts to split it
    into by length, return a list of the string split by that length.
    The final part can be >= the length of the earlier parts in order
    to satisfy the number of parts."""
    if not chars:
        part_list = [""] * parts
        return part_list

    part_len = len(chars) // parts
    part_list = [chars[idx : idx + part_len] for idx in range(0, len(chars), part_len)]

    if len(part_list[-1]) < part_len:
        remainder = part_list.pop()
        part_list[-1] += remainder

    return part_list


def intersect_letters(parts):
    """Given a list of strings, find the letters common to all the strings,
    case sensitive"""
    char_sets = [set(p) for p in parts]
    char_common = set.intersection(*char_sets)

    return list(char_common)


def map_priorities(letters):
    """Map letters to integer priority values"""
    priorities = [PRIORITIES.get(l, 0) for l in letters]
    return priorities
