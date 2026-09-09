file = open("memo.txt", "r")
lines = file.readlines()
file.close()

print("--- Your Memos ---")

for line in lines:
    print(line.strip())