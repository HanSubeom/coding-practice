def add_numbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)

print("Result: " + str(result))

def subtract_numbers(a, b):
    return a - b

result_subtract = subtract_numbers(num1, num2)

print("Result (Subtraction): " + str(result_subtract))
