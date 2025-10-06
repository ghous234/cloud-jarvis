def factorial_iterative(n):
    # Iterative tareeke se factorial calculate karna
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_recursive(n):
    # Recursion ka use kar ke factorial calculate karna
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# User se choice lena
choice = input("Enter 'i' for iterative or 'r' for recursive factorial calculation: ")

# Factorial calculate karna
if choice == 'i':
    num = int(input("Enter a number: "))
    result = factorial_iterative(num)
    print(f"Factorial of {num} using iteration is {result}")
elif choice == 'r':
    num = int(input("Enter a number: "))
    result = factorial_recursive(num)
    print(f"Factorial of {num} using recursion is {result}")
else:
    print("Invalid choice")
