import random


def hangman(word: str):
    wrong: int = 0
    stages: list[str] = [
        "",
        "______      ",
        "|           ",
        "|     |     ",
        "|     0     ",
        "|    /|     ",
        "|    /      ",
    ]
    rletters: list[str] = list(word)
    board: list[str] = ["_"] * len(word)
    win: bool = False
    print("ハングマンへようこそ")

    while wrong < len(stages) - 1:
        print("\n")
        msg: str = "1文字を予想してね: "
        char: str = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e: int = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win: bool = True
            break
    if not win:
        print("\n".join(stages[0 : wrong + 1]))
        print(f"あなたの負け！正解は{word}")


answer_lists: list[str] = ["cat", "dog", "horse"]
choice_number = random.randrange(2)
hangman(answer_lists[choice_number])
