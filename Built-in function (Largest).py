#Write a function to find the largest number of the three user entered numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def largest(num1, num2, num3):
    return max(num1,num2,num3)

print("Largest number is ",largest(num1,num2,num3))
