#Write a python program to print the reverse of the number.
#Ex:12345 -> 54321

num = int(input("Enter a number: "))

rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
