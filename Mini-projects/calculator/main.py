result = 0
while True:
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    if operation == "q":
        print("Calculator closed.")
        break

    if operation not in ["+", "-", "*", "/", "q"]:
        print("Invalid operation. Try again.")
        continue

    num1 = (input("Enter first number: "))
    if num1 == "ans":
        num1 = result
    else:
        num1 = float(num1) 
    num2 = (input("Enter second number: "))
    if num2 == "ans":
        num2 = result
    else:
        num2 = float(num2)

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1 / num2

    print("Result =", result)
