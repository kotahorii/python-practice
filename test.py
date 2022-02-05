from typing import Union


def convert_to_float(x: Union[int, float]):
    try:
        print(float(x))
    except ValueError:
        print("x is not valid")


convert_to_float(3)
