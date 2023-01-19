from collections import namedtuple


Vector2d = namedtuple("Vector2d", ["x", "y"])


DIRECTION_VECTORS = {
    "U": Vector2d(0, 1),
    "D": Vector2d(0, -1),
    "L": Vector2d(-1, 0),
    "R": Vector2d(1, 0),
}


def motion_to_steps(motion):
    """Given a string representing a "motion", with a direction (U, D, L, R)
    and a number of steps, expand into a list of individual step vectors
    representing that motion"""
    direction, distance = motion.strip().split()
    step_vector = DIRECTION_VECTORS.get(direction)
    return [step_vector] * int(distance)


def move_point(step, current):
    """Given a step vector, and a current location vector, calculate the
    result of moving the point by the step (2D vector addition)"""
    return Vector2d(current.x + step.x, current.y + step.y)


def get_vector_distance(start, end):
    """Given two 2D vectors, find the vector representing the distance
    between the two points"""
    return Vector2d(end.x - start.x, end.y - start.y)


def normalize_step(step):
    """Given a step vector, "normalize" it such that the magnitude per
    axis is no more than 1 in the direction of the step vector"""
    normalized = Vector2d(
        x=0 if step.x == 0 else step.x // abs(step.x),
        y=0 if step.y == 0 else step.y // abs(step.y),
    )

    return normalized
