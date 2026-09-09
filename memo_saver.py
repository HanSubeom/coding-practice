memo = input("Enter your memo: ")

file = open("memo.txt", "a")
file.write(memo + "\n")
file.close()

print("Memo saved!")