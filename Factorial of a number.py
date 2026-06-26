#Write a python program to calculate the factorial of a number using while loop.
#Ex: 5=4x3x2x1

num=int(input("Enter a number : "))
fact=1
while num>=1:
    fact=fact*num
    num=num-1
print(f"The Factorial of the number is {fact}")
