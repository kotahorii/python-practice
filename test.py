from typing import Union

facts: dict[str, Union[str, int]] = {}

facts["code"] = "fun"
print(facts["code"])

facts["founded"] = 1997
print(facts["founded"])
