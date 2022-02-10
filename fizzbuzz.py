# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


def ss(number_list: list[int], n: int) -> bool:
    found: bool = False
    for i in number_list:
        if i == n:
            found = True
            break

    return found


numbers: range = range(0, 101)
s1 = ss(list(numbers), 200)
print(s1)
