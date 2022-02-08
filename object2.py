# class PublicPrivateExample:
#     def __init__(self) -> None:
#         self.public = "safe"
#         self._unsafe = "unsafe"

#     def public_method(self) -> None:
#         pass

#     def _unsafe_method(self) -> None:
#         pass


# class Shape:
#     def __init__(self, width: int, len: int) -> None:
#         self.width: int = width
#         self.len: int = len

#     def print_size(self):
#         print(f"{self.width} by {self.len}")


# class Square(Shape):
#     def area(self) -> float:
#         return self.width * self.len

#     def print_size(self) -> None:
#         print(f"I am {self.width} by {self.len}")


# a_square: Square = Square(20, 20)
# a_square.print_size()


# class Person:
#     def __init__(self, name: str) -> None:
#         self.name: str = name


# class Dog:
#     def __init__(self, name: str, breed: str, owner: Person) -> None:
#         self.name: str = name
#         self.breed: str = breed
#         self.owner: Person = owner


# mick: Person = Person("Mick Jagger")
# stan: Dog = Dog("Stanley", "Bulldog", mick)
# print(stan.owner.name)


# class Rectangle:
#     def __init__(self, edge_size1: int, edge_size2: int) -> None:
#         self.edge_size1: int = edge_size1
#         self.edge_size2: int = edge_size2

#     def calculate_perimeter(self) -> float:
#         return (self.edge_size1 + self.edge_size2) * 2


# class Square:
#     def __init__(self, edge_size: int) -> None:
#         self.edge_size: int = edge_size

#     def change_size(self, changed_size: int):
#         self.edge_size += changed_size

#     def calculate_perimeter(self) -> float:
#         return self.edge_size * 4


# rectangle: Rectangle = Rectangle(2, 3)
# square: Square = Square(3)
# square.change_size(1)
# print(square.edge_size)


# class Shape:
#     def what_am_i(self) -> None:
#         print("I am a shape")


# class Rectangle(Shape):
#     pass


# class Square(Shape):
#     pass


# rectangle: Rectangle = Rectangle()
# rectangle.what_am_i()


# class Rider:
#     def __init__(self, name: str) -> None:
#         self.name: str = name


# class Horse:
#     def __init__(self, name: str, rider: Rider) -> None:
#         self.name: str = name
#         self.rider = rider


# rider: Rider = Rider("Takashi")
# horse: Horse = Horse("uma", rider)

# print(horse.rider.name)
