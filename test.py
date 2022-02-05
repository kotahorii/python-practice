from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

file = f"file_{today}.txt"
print(file)
