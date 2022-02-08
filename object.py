from math import pi


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def area(self) -> float:
        return pi * self.radius**2


circle: Circle = Circle(10)
print(circle.area())


class Triangle:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

    def area(self) -> float:
        return self.width * self.height / 2


triangle: Triangle = Triangle(2, 3)
print(triangle.area())


class Hexagon:
    def __init__(self, edge_size: int) -> None:
        self.edge_size = edge_size

    def calculate_permeter(self) -> float:
        return self.edge_size * 6


hexagon: Hexagon = Hexagon(3)
print(hexagon.calculate_permeter())
