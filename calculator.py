# Define functions for basic arithmetic operations
def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers, handles division by zero"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Display available operations to the user
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Start a loop for continuous calculation until the user chooses to exit
while True:
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            # Get numbers from the user and convert them to floating-point numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue # Go back to the start of the loop

        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operator = '/'
        
        # Print the equation and the result
        print(f"{num1} {operator} {num2} = {result}")
        
    else:
        print("Invalid choice")
        
    # Ask if the user wants to perform another calculation or exit
    next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if next_calculation == "no":
        print("Calculator session ended. Goodbye!")
        break