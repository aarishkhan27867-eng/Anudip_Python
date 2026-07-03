# Q2.Write a Python function to find whether a number is prime.

# Function to check prime number
def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Not a Prime Number")

# Take input from the user
num = int(input("Enter a number: "))

# Call the function
check_prime(num)

# Output
"""
Enter a number: 6
Not a Prime Number

Enter a number: 13
Prime Number
"""
