#Write a program to check if a number is perfect or not.

num=int(input("Enter a number: "))

div=0

for i in range(1,num) :
    if (num % i == 0) :
        div=div+i

if div==num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
