import math


def calculate_magnitude(vector):
    return math.sqrt(
        sum(
            [n ** 2 for n in vector]
        )
    )


def vector_between_two_points(origin, terminal):
    x_origin, y_origin = origin
    x_terminal, y_terminal = terminal
    return (
        x_terminal - x_origin,
        y_terminal - y_origin,
    )


def reduce_vector(vector, max_magnitude):
    magnitude = calculate_magnitude(vector)

    if magnitude <= max_magnitude:
        return vector

    factor = max_magnitude / magnitude
    d_x, d_y = vector

    return (
        d_x * factor,
        d_y * factor,
    )


def reduced_vector_between_two_points(origin, terminal, max_magnitude):
    resultant = vector_between_two_points(origin, terminal)

    return reduce_vector(resultant, max_magnitude) \
        if calculate_magnitude(resultant) > max_magnitude else resultant


def is_point_in_range(origin, terminal, range_):
    return calculate_magnitude(
        vector_between_two_points(origin, terminal)
    ) > range_
