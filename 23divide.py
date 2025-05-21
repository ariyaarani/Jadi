# Author: Mohammad Reza Arani

def divide(a, b):
    return a / b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = divide(num1, num2)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    print("Result:", result)
finally:
    print("Program finished.")
