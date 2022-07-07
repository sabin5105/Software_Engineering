def calc_rect_area(w, h):
    return w * h


def calc_triangle_area(base, h):
    return calc_rect_area(base, h) / 2


def calc_rect_inner_angle():
    return 360


def calc_triangle_inner_angle():
    return calc_rect_inner_angle() / 2