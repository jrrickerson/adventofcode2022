import itertools


def convert_int_list(str_list):
    """Convert a list of strings into a list of integers, preserving blank lines
    by converting them to None as group separators"""
    return [int(line) if line.strip() else None for line in str_list]


def partition_list(str_list):
    """Partition a list of strings into a list of lists, breaking at each
    empty entry.
    ["1", "2", "3", "", "4", "5"] -> [["1", "2", "3"], ["4", "5"]]"""
    if not str_list:
        return []

    return [list(group) for key, group in
            itertools.groupby(str_list, key=lambda x: bool(x)) if key is True]


def sum_partitions(partitions):
    return [sum(part) for part in partitions]
