# Q3.Write a Python function to print Fibonacci series.

# Function to print Fibonacci series
def fibonacci(num):
    a=0
    b=1

    for i in range(num):
        print(a, end=" ")
        c=a+b
        a=b
        b=c

# Take input from the user
num = int(input("Enter the number of terms: "))

# Call the function
fibonacci(num)

# Output
"""
Enter the number of terms: 7
0 1 1 2 3 5 8
"""
