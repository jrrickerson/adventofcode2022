import solve
import utils


def test_motion_to_steps_up():
    motion = "U 1"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 1
    assert steps[0].y == 1
    assert steps[0].x == 0


def test_motion_to_steps_down():
    motion = "D 1"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 1
    assert steps[0].y == -1
    assert steps[0].x == 0


def test_motion_to_steps_left():
    motion = "L 1"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 1
    assert steps[0].y == 0
    assert steps[0].x == -1


def test_motion_to_steps_right():
    motion = "R 1"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 1
    assert steps[0].y == 0
    assert steps[0].x == 1


def test_motion_to_steps_expand_distance():
    motion = "U 7"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 7
    for step in steps:
        assert step.y == 1
        assert step.x == 0


def test_motion_to_steps_multi_digit_distance():
    motion = "D 27"

    steps = utils.motion_to_steps(motion)

    assert len(steps) == 27
    for step in steps:
        assert step.y == -1
        assert step.x == 0


def test_move_point_up_from_origin():
    start = utils.Vector2d(0, 0)
    step = utils.Vector2d(0, 1)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(0, 1)


def test_move_point_down_from_origin():
    start = utils.Vector2d(0, 0)
    step = utils.Vector2d(0, -1)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(0, -1)


def test_move_point_left_from_origin():
    start = utils.Vector2d(0, 0)
    step = utils.Vector2d(-1, 0)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(-1, 0)


def test_move_point_right_from_origin():
    start = utils.Vector2d(0, 0)
    step = utils.Vector2d(1, 0)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(1, 0)


def test_move_point_diagonal_from_origin():
    start = utils.Vector2d(0, 0)
    step = utils.Vector2d(1, 1)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(1, 1)


def test_move_point_non_origin():
    start = utils.Vector2d(1, 6)
    step = utils.Vector2d(0, 1)

    current = utils.move_point(step, start)

    assert current == utils.Vector2d(1, 7)


def test_get_vector_distance_same_point():
    head = utils.Vector2d(0, 0)
    tail = utils.Vector2d(0, 0)

    diff = utils.get_vector_distance(head, tail)

    assert diff == utils.Vector2d(0, 0)


def test_get_vector_distance_x_axis():
    head = utils.Vector2d(2, 0)
    tail = utils.Vector2d(0, 0)

    diff = utils.get_vector_distance(head, tail)

    assert diff == utils.Vector2d(-2, 0)


def test_get_vector_distance_y_axis():
    head = utils.Vector2d(0, 2)
    tail = utils.Vector2d(0, 0)

    diff = utils.get_vector_distance(head, tail)

    assert diff == utils.Vector2d(0, -2)


def test_get_vector_distance_non_orthogonal():
    head = utils.Vector2d(2, 3)
    tail = utils.Vector2d(1, 1)

    diff = utils.get_vector_distance(head, tail)

    assert diff == utils.Vector2d(-1, -2)


def test_normalize_step_origin():
    step = utils.Vector2d(0, 0)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(0, 0)


def test_normalize_step_x_axis():
    step = utils.Vector2d(4, 0)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(1, 0)


def test_normalize_step_y_axis():
    step = utils.Vector2d(0, 12)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(0, 1)


def test_normalize_step_positive():
    step = utils.Vector2d(5, 7)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(1, 1)


def test_normalize_step_negative():
    step = utils.Vector2d(-3, -2)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(-1, -1)


def test_normalize_step_mixed_signs():
    step = utils.Vector2d(3, -2)

    normalized = utils.normalize_step(step)

    assert normalized == utils.Vector2d(1, -1)


def test_part_1_sample_input():
    input_data = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    result = solve.part_1(input_data)

    assert result == 13


def test_part_2_sample_input():
    input_data = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    result = solve.part_2(input_data)

    assert result == 1


def test_part_2_sample_input_2():
    input_data = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]

    result = solve.part_2(input_data)

    assert result == 36
