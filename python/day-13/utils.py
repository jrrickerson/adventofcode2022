import json


def parse_packet(line):
    try:
        return json.loads(line)
    except:
        return None


def compare(left, right):
    """Compare two "packets" to determine order.
    Packets consist of lists of data, which can take the form of integers
    or lists themselves.
    Returns:
        -1 if left < right
         1 if left > right
         0 if left == right
    """
    l_type = type(left)
    r_type = type(right)

    # print(f"Comparing {left} < {right}")
    if l_type is int and r_type is int:
        return 0 if left == right else -1 if left < right else 1
    if l_type is int and r_type is list:
        return compare([left], right)
    if l_type is list and r_type is int:
        return compare(left, [right])
    if l_type is list and r_type is list:
        if not left and not right:
            # print("Empty lists")
            return 0
        if not left and right:
            # print("Left is empty")
            return -1
        if left and not right:
            # print("Right is empty")
            return 1
        order = compare(left[0], right[0])
        # print("Compare list head")
        if order:
            return order
        # print("Compare list tail")
        return compare(left[1:], right[1:])
