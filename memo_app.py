def add_memo():
    memo = input("Enter your memo: ")
    file = open("memo.txt", "a")
    file.write(memo + "\n")
    file.close()
    print("Memo saved!")

def show_memos():
    file = open("memo.txt", "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        print(line.strip())

choice = input("1. Add memo  2. Show memos  3. Exit\nChoose: ")

while choice != "3":
    if choice == "1":
        add_memo()
    elif choice == "2":
        show_memos()
    else:
        print("Invalid choice.")
    
    choice = input("1. Add memo  2. Show memos  3. Exit\nChoose: ")

print("Goodbye!")