from shape_oo import Rect, Triangle


def test_calc_rect_area():
    assert Rect("red", 2, 4).area() == 8
    assert Rect("red", 0, 4).area() == 0
    assert Rect("red", 4, 0).area() == 0


def test_calc_triangle_area():
    assert Triangle("red", 2, 4).area() == 4
    assert Triangle("red", 0, 4).area() == 0
    assert Triangle("red", 4, 0).area() == 0


def test_calc_rect_inner_angle():
    assert Rect("red", 2, 4).inner_angle() == 360


def test_calc_triangle_inner_angle():
    assert Triangle("red", 2, 4).inner_angle() == 180


def test_sum_of_areas():
    shapes = [
        Rect("red", 4, 2),
        Rect("red", 3, 3),
        Triangle("red", 2, 3),
    ]

    assert sum(s.area() for s in shapes) == 20


def test_has_same_area():
    s0 = Rect("red", 2, 4)
    s1 = Triangle("red", 4, 4)
    assert s0.has_same_area(s1)