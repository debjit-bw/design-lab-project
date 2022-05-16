import math


def position_to_irl(
    y_axis_val,
    height_irl,
    frame_bound_y_start,
    frame_bound_y_end,
    distance_from_velocity_vector=math.inf,
):
    midpoint = (frame_bound_y_end + frame_bound_y_start) / 2
    proportion = (y_axis_val - midpoint) / (frame_bound_y_end - frame_bound_y_start)
    apparent_height = height_irl * proportion
    phi = math.atan(apparent_height / distance_from_velocity_vector)
    return apparent_height, apparent_height / math.cos(phi)
