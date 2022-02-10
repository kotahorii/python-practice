# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


# def ss(number_list: list[int], n: int) -> bool:
#     found: bool = False
#     for i in number_list:
#         if i == n:
#             found = True
#             break

#     return found


# numbers: range = range(0, 101)
# s1 = ss(list(numbers), 200)
# print(s1)


# def palindrome(word: str) -> bool:
#     word = word.lower()
#     return word[::-1] == word


# print(palindrome("Mother"))
# print(palindrome("Mom"))


# def anagram(w1: str, w2: str) -> bool:
#     w1 = w1.lower()
#     w2 = w2.lower()
#     return sorted(w1) == sorted(w2)


# print(anagram("iceman", "cinema"))
# print(anagram("leaf", "tree"))


def count_characters(string: str) -> None:
    count_dict: dict[str, int] = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)


count_characters("Dynasty")
