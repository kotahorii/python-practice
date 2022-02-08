# class PublicPrivateExample:
#     def __init__(self) -> None:
#         self.public = "safe"
#         self._unsafe = "unsafe"

#     def public_method(self) -> None:
#         pass

#     def _unsafe_method(self) -> None:
#         pass


class Shape:
    def __init__(self, width: int, len: int) -> None:
        self.width: int = width
        self.len: int = len

    def print_size(self):
        print(f"{self.width} by {self.len}")


class Square(Shape):
    def area(self) -> float:
        return self.width * self.len

    def print_size(self) -> None:
        print(f"I am {self.width} by {self.len}")


a_square: Square = Square(20, 20)
a_square.print_size()
