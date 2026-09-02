numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

    total = sum(numbers)
    average = total / len(numbers)

print("Numbers: " + str(numbers))
print("Total: " + str(total))
print("Average: " + str(average))