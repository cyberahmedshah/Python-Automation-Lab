while True:
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    if operation == "q":
        print("Calculator closed.")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

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
