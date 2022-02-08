# from typing import Any


# class Square:
#     square_list: list[Any] = []

#     def __init__(self) -> None:
#         self.square_list.append(self)


# square1: Square = Square()
# square2: Square = Square()
# square3: Square = Square()

# print(Square.square_list)


# class Square:
#     def __init__(self, len: int) -> None:
#         self.len: int = len

#     def __repr__(self) -> str:
#         return f"{self.len} by {self.len} by {self.len} by {self.len}"


# square: Square = Square(29)
# print(square)

from typing import Any


class SampleObj:
    pass


obj1: SampleObj = SampleObj()
obj2: SampleObj = SampleObj()


def is_same_obj(obj1: Any, obj2: Any) -> bool:
    return obj1 is obj2


print(is_same_obj(obj1, obj2))
