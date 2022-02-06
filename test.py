# lists: list[str] = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

# for i, list in enumerate(lists):
#     print(f"{i}: {list}")

list1: list[int] = [8, 19, 148, 4]
list2: list[int] = [9, 1, 33, 83]
new_list: list[int] = []

for i in list1:
    for j in list2:
        new_list.append(i * j)

print(new_list)
