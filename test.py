correct_answers: list[int] = [3, 7, 10]

while True:
    answer: str = input("数字を入力するか、qで終了します: ")

    if answer == "q":
        break
    else:
        try:
            correct_or_wrong: str = "正解" if int(answer) in correct_answers else "不正解"
            print(correct_or_wrong)
            break
        except ValueError:
            continue
