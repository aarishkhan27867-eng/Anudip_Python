#Write a program to check whether the number is armstrong number or not.
#Ex: 153 it shoul give the same value on summation of cubing all numbers

num=(int(input("Enter the number : ")))

temp=num
arm=0
digit=0
while temp>=1:
    digit=temp%10
    arm=arm+(digit*digit*digit)
    temp//=10

if num ==arm:
    print("It is an Armstrong number")
else:
    print("Not a Armstrong number")
