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

def delete_memo():
    file = open("memo.txt", "r")
    lines = file.readlines()
    file.close()

    print("--- Your Memos ---")
    for i, line in enumerate(lines):
        print(str(i + 1) + ": " + line.strip())

    choice = int(input("Enter the number to delete: "))

    lines.pop(choice - 1)

    file = open("memo.txt", "w")
    for line in lines:
        file.write(line)
    file.close()

    print("Memo deleted!")

choice = input("1. Add memo  2. Show memos  3. Exit  4. Delete memo\nChoose: ")

while choice != "3":
    if choice == "1":
        add_memo()
    elif choice == "2":
        show_memos()
    elif choice == "4":
        delete_memo()
    else:
        print("Invalid choice.")

    choice = input("1. Add memo  2. Show memos  3. Exit  4. Delete memo\nChoose: ")

print("Goodbye!")