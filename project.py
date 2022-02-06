import csv

lists: list[list[str]] = [
    ["トップガン", "リスキービジネス", "マイノリティ・リポート"],
    ["タイタニック", "レブナント", "インセプション"],
    ["トレーニングデイ", "マノンファイア", "フライト"],
]


with open("list.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for list in lists:
        w.writerow(list)
