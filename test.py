# def f(x: int, y: int):
#     return x * y


# result = f(2, 3)
# print(result)

# print(len("Python"))

# age: str = input("Enter your age: ")
# int_age = int(age)
# if int_age < 21:
#     print("You are young!")
# else:
#     print("You are old")


# def even_odd(x: int):
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# even_odd(3)
# even_odd(2)


def f(x: int = 2):
    return x**x


print(f())
print(f(4))
