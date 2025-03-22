def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
