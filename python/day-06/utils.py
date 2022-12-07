def is_set_span(span):
    """Determine if the span provided is a set of unique values"""
    return len(span) == len(set(span))


def find_set_span(sequence, size=4):
    """Given a sequence and a target set size, find the first span of the
    size that is a unique set of values"""
    for i in range(len(sequence)):
        span = sequence[i : i + size]
        if len(span) < size:
            return None
        if is_set_span(span):
            return i
    else:
        return None
