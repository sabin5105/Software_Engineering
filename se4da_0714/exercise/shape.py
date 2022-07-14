import math


def calc_rect_area(w, h):
    """직사각형의 면적을 계산한다

    Args:
        w (float): 너비
        h (float): 높이

    Returns:
        float: 면적
    """
    return w * h


def calc_rect_inner_angle():
    """직사각형의 내각의 합을 계산한다"""
    return 360


def calc_triangle_area(base, h):
    """삼각형의 너비를 계산한다

    Args:
        base (float): 밑변
        h (float): 높이

    Returns:
        float: 면적
    """
    return calc_rect_area(base, h) / 2


def calc_triangle_inner_angle():
    """삼각형의 내각의 합을 계산한다

    Returns:
        float: 내각의 합
    """
    return calc_rect_inner_angle() / 2


def calc_circle_area(r):
    """정원의 면적을 구한다

    Args:
        r (float): 반지름

    Returns:
        float: 면적
    """
    return math.pi * r**2


def calc_circle_inner_angle():
    """정원의 내각의 합을 계산한다

    Returns:
        float: 내각의 합
    """
    return 0


def calc_area(s):
    """도형의 면적을 계산한다

    Args:
        s (dict): 도형 정보를 담고 있는 dict

    Raises:
        ValueError: 지원하지 않는 type인 경우 발생

    Returns:
        float: 면적
    """
    if s['type'] == 'rect':
        return calc_rect_area(s['w'], s['h'])
    if s['type'] == 'triangle':
        return calc_triangle_area(s['b'], s['h'])
    if s['type'] == 'circle':
        return calc_circle_area(s['r'])
    raise ValueError(f'Uknown shape: {s["type"]}')


def has_same_area(s0, s1):
    """두 도형의 면적이 같은지 검사한다

    Args:
        s0 (dict): 도형0
        s1 (dict): 도형1

    Returns:
        bool: 면적이 같으면 True, 아니면 False
    """
    a0 = calc_area(s0)
    a1 = calc_area(s1)
    return a0 == a1
