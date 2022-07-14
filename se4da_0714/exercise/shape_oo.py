import math


class Shape:

    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError()

    def inner_angle(self):
        raise NotImplementedError()

    def report_color(self):
        return f'My color is {self.color}'

    def has_same_area(self, o):
        return self.area() == o.area()


class Rect(Shape):

    def __init__(self, color, w, h):
        super().__init__(color)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def inner_angle(self):
        return 360


class Triangle(Shape):

    def __init__(self, color, b, h):
        super().__init__(color)
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h / 2

    def inner_angle(self):
        return 180


class Circle(Shape):

    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    def area(self):
        return self.r**2 * math.pi

    def inner_angle(self):
        return 0
