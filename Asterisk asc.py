"""write a program to print pattern
*
**
***
****
*****
"""
#Solution 1
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(i * "*")

#Solution 2
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(i):
        print("*", end="")
    print()

