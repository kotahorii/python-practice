from typing import Union

lists = []

rap: list[Union[str, list[str]]] = ["1", "2", "3"]
rock: list[str] = ["a", "b", "c"]

rap.append(rock)
print(rap)
