def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    try:
        num1 = input("Enter first number: ").strip()
        num2 = input("Enter second number: ").strip()

        # Ensure input is not empty before converting to int
        num1 = int(num1) if num1 else 0
        num2 = int(num2) if num2 else 0

        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
