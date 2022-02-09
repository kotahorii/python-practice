from random import shuffle
from typing import Any


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [
        "",
        "",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, value: int, suit: int) -> None:
        self.value: int = value
        self.suit: int = suit

    def __lt__(self, c2: Any) -> bool:
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2: Any) -> bool:
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self) -> str:
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self) -> str:
        if len(self.cards) == 0:
            return ""
        return str(self.cards.pop())


class Player:
    def __init__(self, name: str) -> None:
        self.wins: int = 0
        self.card: None = None
        self.name: str = name


class Game:
    def __init__(self) -> None:
        name1: str = input("プレーヤー1の名前")
        name2: str = input("プレーヤー2の名前")

        self.deck: Deck = Deck()

        self.p1: Player = Player(name1)
        self.p2: Player = Player(name2)

    def wins(self, winner: str) -> None:
        w: str = f"このラウンドは{winner}が勝ちました！"
        print(w)

    def draw(self, p1n: str, p1c: str, p2n: str, p2c: str) -> None:
        d: str = f"{p1n}は{p1c}、{p2n}は{p2c}を引きました。"
        print(d)

    def play_game(self):
        cards: list[Card] = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            m: str = "q で終了、それ以外のキーでプレイ"
            response: str = input(m)
            if response == "q":
                break
            p1c: str = self.deck.rm_card()
            p2c: str = self.deck.rm_card()
            p1n: str = self.p1.name
            p2n: str = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win: str = self.winner(self.p1, self.p2)
        print(f"ゲーム終了、{win}の勝利です！")

    def winner(self, p1: Player, p2: Player) -> str:
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"


game: Game = Game()
game.play_game()
