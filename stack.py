from typing import Union


class Stack:
    def __init__(self) -> None:
        self.items: list[Union[str, int]] = []

    def is_empty(self) -> bool:
        return not self.items

    def push(self, item: Union[str, int]) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self) -> Union[str, int]:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


stack: Stack = Stack()
# stack.push(1)
# item = stack.pop()
# print(stack.is_empty(), item)

# for i in range(0, 6):
#     stack.push(i)

# print(stack.peek())
# print(stack.size())

# for c in "yesterday":
#     stack.push(c)

# reverse: str = ""

# while stack.size():
#     reverse += str(stack.pop())

# print(reverse)

items: list[int] = [1, 2, 3, 4, 5]
new_items: list[Union[str, int]] = []
for item in items:
    stack.push(item)
    print(stack.items)
    new_item = stack.pop()
    new_items.insert(0, new_item)

print(new_items)
