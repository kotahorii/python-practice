# books: dict[str, str] = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
# del books["The Trial"]

# print(books)

songs: dict[str, str] = {"1": "fun", "2": "blue", "3": "me", "4": "floor", "5": "live"}
n: str = input("数字を入力してください: ")

if n in songs:
    song: str = songs[n]
    print(song)
else:
    print("見つかりません")
