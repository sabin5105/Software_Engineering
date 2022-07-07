from shape import (calc_rect_area, calc_rect_inner_angle, calc_triangle_area,
                   calc_triangle_inner_angle)


def test_calc_rect_area():
    assert calc_rect_area(2, 4) == 8
    assert calc_rect_area(0, 4) == 0
    assert calc_rect_area(4, 0) == 0


def test_calc_triangle_area():
    assert calc_triangle_area(2, 4) == 4
    assert calc_triangle_area(0, 4) == 0
    assert calc_triangle_area(4, 0) == 0


def test_calc_rect_inner_angle():
    assert calc_rect_inner_angle() == 360


def test_calc_triangle_inner_angle():
    assert calc_triangle_inner_angle() == 180


def test_sum_of_areas():
    shapes = [
        {'type': 'rect', 'w': 4, 'h': 2},  # 8
        {'type': 'rect', 'w': 3, 'h': 3},  # 9
        {'type': 'triangle', 'b': 2, 'h': 3},  # 3
    ]
    result = 0
    for s in shapes:
        if s['type'] == 'rect':
            area = calc_rect_area(s['w'], s['h'])
        elif s['type'] == 'triangle':
            area = calc_triangle_area(s['b'], s['h'])
        else:
            raise ValueError(f'Unknown shape: {s["type"]}')
        result += area
    assert result == 20