# Q1.Write a Python function to calculate factorial of a number.

# Function to calculate factorial
def check_factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact * i
    print("Factorial =",fact)

# Take input from the user
num = int(input("Enter a number: "))

# Call the function
check_factorial(num)

# Output
"""
Enter a number: 5
Factorial = 120
"""
